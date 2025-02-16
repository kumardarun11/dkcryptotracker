import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.graph_objects as go
import time
import ta
import ccxt  # Binance API Wrapper
from prophet import Prophet  # AI Forecasting
from forex_python.converter import CurrencyRates
import requests
import requests_cache

requests_cache.install_cache('currency_cache', expire_after=3600)  # Cache for 1 hour
requests_cache.clear()  # Clear cache before fetching new rates


def get_conversion_rate(base="USD", target="INR"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["rates"].get(target, 1)  # Default to 1 if currency not found
    except (requests.exceptions.RequestException, ValueError):
        return 1  # Fallback to 1 if API fails


# Binance API URL for fetching live prices
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/24hr"

# Cryptocurrencies to track
CRYPTO_PAIRS = ["BTC/USDT", "ETH/USDT", "BNB/USDT", "XRP/USDT", "ADA/USDT", "DOGE/USDT", "SOL/USDT"]

# Initialize Binance API (ccxt)
import ccxt
binance = ccxt.binance({
    'apiKey': 'ZkkFxuvMBhtu5hK3qfmwTWk5kME0VqiFp3j8eim7SfiGCoF2ocBjGPLaUFNBapjF',
    'secret': 'scFOoOLEJHwF7KZnVcC8HVGK9DTa7PR4ZCRPD0IZ5SQVTvdsLbYZw8rc9sgPVcGw',
    'enableRateLimit': True,
    'options': {'adjustForTimeDifference': True},
})
currency_rates = CurrencyRates()

def get_crypto_pairs(base_currency="USD"):
    return [pair.replace("USDT", base_currency) for pair in CRYPTO_PAIRS]


# Function to fetch real-time price data
def get_crypto_data(base_currency="USD"):
    prices = []
    conversion_rate = get_conversion_rate("USD", base_currency)  # Convert prices
    
    for pair in CRYPTO_PAIRS:
        ticker = binance.fetch_ticker(pair)
        converted_price = ticker['last'] * conversion_rate
        converted_high = ticker['high'] * conversion_rate
        converted_low = ticker['low'] * conversion_rate
        converted_volume = ticker['baseVolume'] * conversion_rate

        # Change Symbol to BTC/INR, ETH/INR if needed
        formatted_pair = pair.replace("USDT", base_currency)

        prices.append([
            formatted_pair, converted_price, ticker['percentage'], converted_high, converted_low, converted_volume
        ])

    df = pd.DataFrame(prices, columns=["Symbol", "Price", "24h % Change", "High", "Low", "Volume"])
    return df


# Function to fetch historical OHLCV (candlestick) data
def get_historical_data(symbol, timeframe='1h', limit=50):
    ohlcv = binance.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["Time", "Open", "High", "Low", "Close", "Volume"])
    df["Time"] = pd.to_datetime(df["Time"], unit='ms')
    return df

# Function to add technical indicators
def add_technical_indicators(df):
    df["SMA_10"] = ta.trend.sma_indicator(df["Close"], window=10)
    df["SMA_50"] = ta.trend.sma_indicator(df["Close"], window=50)
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)
    df["Bollinger_Upper"], df["Bollinger_Middle"], df["Bollinger_Lower"] = ta.volatility.bollinger_hband(df["Close"]), ta.volatility.bollinger_mavg(df["Close"]), ta.volatility.bollinger_lband(df["Close"])
    return df

# Function for AI-based price prediction
def predict_future_prices(df):
    prophet_df = df.rename(columns={"Time": "ds", "Close": "y"})
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=24, freq="h")
    forecast = model.predict(future)
    return forecast

# Streamlit UI
st.set_page_config(page_title="🚀 DK Crypto Tracker", layout="wide")

st.title("📊 DK Real-Time Crypto Tracker")
st.write("Live Binance prices with technical analysis, AI forecasting, and alerts.")

# Sidebar settings
st.sidebar.header("🔧 Settings")
base_currency = st.sidebar.selectbox("🌍 Select Base Currency", ["USD", "INR", "EUR", "GBP"], index=0)
refresh_rate = st.sidebar.slider("⏳ Refresh Rate (seconds)", 5, 60, 10)
alert_threshold = st.sidebar.slider("🚨 Alert Threshold (%)", 1, 10, 5)

# Fetch & display live prices
st.subheader("💰 Live Crypto Prices")
crypto_data = get_crypto_data(base_currency)
st.dataframe(crypto_data.style.map(lambda x: "color: red" if x < 0 else "color: green", subset=["24h % Change"]))


# Choose cryptocurrency for analysis
st.subheader("📈 Technical Analysis")
formatted_crypto_pairs = get_crypto_pairs(base_currency)  # Get dynamically updated pairs
selected_crypto = st.selectbox("Select Cryptocurrency", formatted_crypto_pairs)

# Fetch & display candlestick chart
st.subheader("📊 Candlestick Chart with Indicators")
actual_crypto_pair = selected_crypto.replace(base_currency, "USDT")  # Convert back to USDT for API call
historical_data = get_historical_data(actual_crypto_pair)
historical_data = add_technical_indicators(historical_data)

fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=historical_data["Time"],
    open=historical_data["Open"],
    high=historical_data["High"],
    low=historical_data["Low"],
    close=historical_data["Close"],
    name="Candlestick"
))
fig.update_layout(title=f"{selected_crypto.replace('USDT', base_currency)} Price Analysis", xaxis_title="Date", yaxis_title=f"Price ({base_currency})")
st.plotly_chart(fig)

# RSI Indicator
st.subheader("📉 RSI (Relative Strength Index)")
st.line_chart(historical_data.set_index("Time")["RSI"])

# AI Price Prediction
st.subheader("🔮 AI Price Prediction")
forecast = predict_future_prices(historical_data)
st.line_chart(forecast.set_index("ds")["yhat"])

# Portfolio Tracker
st.subheader("💼 Portfolio Tracker")
st.write("📢 Enter your holdings below:")
crypto_input = st.text_input("Enter coin (e.g., BTC, ETH):").upper()
amount_input = st.number_input("Enter amount:", min_value=0.0, format="%.6f")
if crypto_input and amount_input > 0:
    price = crypto_data.loc[crypto_data["Symbol"] == f"{crypto_input}/{base_currency}", "Price"].values[0]
    st.write(f"💰 Your {crypto_input} is worth: **{price * amount_input:.2f} {base_currency}**")

# Refresh Data 
if st.sidebar.button("🔄 Refresh Data"):
    st.rerun()

# ℹ Developer Info
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 Developer Info")
st.sidebar.write("**Name:** D ARUN KUMAR")
st.sidebar.write("📧 Email: kumardarun11@gmail.com")
st.sidebar.write("[GitHub](https://github.com/kumardarun11) | [LinkedIn](https://linkedin.com/in/kumardarun11)")
