Here's your **README.md** file for GitHub:  

---

### 📊 DK Crypto Tracker  
🚀 **Real-time Binance Cryptocurrency Tracker with AI Forecasting & Technical Analysis**  

---

## 🌟 Features  
✅ **Live crypto prices** from Binance  
✅ **AI price prediction** using Facebook Prophet  
✅ **Technical indicators** (SMA, RSI, Bollinger Bands)  
✅ **Candlestick charts** with Plotly  
✅ **Portfolio tracker** to monitor holdings  
✅ **Multi-currency support** (USD, INR, EUR, GBP)  

---

## 🛠 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/dk-crypto-tracker.git
cd dk-crypto-tracker
```

### 2️⃣ Create a Virtual Environment  
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Binance API Keys  
1. **Create Binance API keys** from [Binance API Management](https://www.binance.com/en/my/settings/api-management)  
2. **Enable Spot & Margin Trading** permissions  
3. **Store API keys securely in Streamlit secrets**  

#### 🔑 **For Local Development** (`.env` file)  
```
BINANCE_API_KEY="your_api_key_here"
BINANCE_API_SECRET="your_api_secret_here"
```

#### 🔐 **For Streamlit Cloud** (`secrets.toml`)  
```
[binance]
api_key = "your_api_key_here"
api_secret = "your_api_secret_here"
```

---


## 📸 Screenshots

Add some screenshots of the app running locally or deployed on Streamlit.

### 1️⃣ Live Crypto Prices
![image](https://github.com/user-attachments/assets/a3389edd-533d-4972-ae78-bd33792fc5b5)

### 2️⃣ Technical Analysis & Indicators
![image](https://github.com/user-attachments/assets/780be120-91b5-47de-816e-215744fb19ed)

### 3️⃣ RSI (Relative Strength Index) & AI Price Prediction 
![image](https://github.com/user-attachments/assets/dcd76363-1135-4043-99c1-d8bdb3606879)

### 4️⃣ Portfolio Tracker
![image](https://github.com/user-attachments/assets/78c753cb-d20f-424e-8937-2c76cb128a59)


## 🚀 Running the App Locally  
```sh
streamlit run app.py
```
✅ Open `http://localhost:8501` in your browser.

---

## 🌍 Deploying on Streamlit Cloud  
1️⃣ **Go to** [Streamlit Cloud](https://share.streamlit.io/)  
2️⃣ **Click "New App" → Select GitHub Repository**  
3️⃣ **Add API keys in Secrets Management**  
4️⃣ **Click Deploy 🚀**  

---

## ⚡ Tech Stack  
- **Streamlit** → UI Framework  
- **CCXT** → Binance API Wrapper  
- **Plotly** → Charts & Data Visualization  
- **TA-Lib** → Technical Indicators  
- **Prophet** → AI Forecasting  
- **Pandas & NumPy** → Data Handling  

---

## ❌ Debugging Issues  

### 🔴 `ccxt.base.errors.ExchangeNotAvailable`?  
✔ **Try These Fixes:**  
- **Check API Key Permissions** (Spot & Margin enabled)  
- **Test Binance API Request on Streamlit Cloud:**  
  ```python
  import requests
  url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  response = requests.get(url)
  print(response.status_code, response.text)
  ```
- **Ensure `requirements.txt` is updated**  
- **Use VPN** if Binance is restricted in your region  

---

## 👨‍💻 Developer  

👤 **D ARUN KUMAR**  
🔗 **LinkedIn:** www.linkedin.com/in/kumardarun11  
📧 **Email:** kumardarun11@example.com  
🔗 **GitHub:** [kumardarun11](https://github.com/kumardarun11)  

---

### ⭐ **Like This Project?**  
Give it a ⭐ on [GitHub](https://github.com/kumardarun11/dkcryptotracker) & Share it! 🚀  

Let me know if you need any changes! 🚀
