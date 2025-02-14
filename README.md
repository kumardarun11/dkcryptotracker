🚀 DK Crypto Tracker
📊 Real-time Binance Cryptocurrency Tracker with AI Forecasting & Technical Analysis

📌 Features
✅ Live cryptocurrency prices from Binance
✅ AI-based price prediction using Facebook Prophet
✅ Technical indicators (SMA, RSI, Bollinger Bands)
✅ Candlestick charts with Plotly
✅ Portfolio tracker to monitor holdings
✅ Supports multiple base currencies (USD, INR, EUR, GBP)

🛠️ Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/yourusername/dk-crypto-tracker.git
cd dk-crypto-tracker
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Binance API Keys
Go to Binance API Management
Create a new API key (Enable Spot & Margin trading)
Add your keys to secrets.toml (for Streamlit Cloud)
🔑 secrets.toml format:
ini
Copy
Edit
[binance]
api_key = "your_api_key_here"
api_secret = "your_api_secret_here"
🚀 Running the App Locally
sh
Copy
Edit
streamlit run app.py
✅ Open http://localhost:8501 in your browser.

🌍 Deployment on Streamlit Cloud
1️⃣ Go to Streamlit Cloud
2️⃣ Click "New App" → Select GitHub Repository
3️⃣ Add API keys in Secrets Management
4️⃣ Click Deploy 🚀

⚡ Technologies Used
Streamlit (UI Framework)
CCXT (Binance API Wrapper)
Plotly (Charts & Data Visualization)
TA-Lib (Technical Indicators)
Prophet (AI Forecasting)
Pandas & NumPy (Data Handling)
🔥 Issues & Debugging
❌ ccxt.base.errors.ExchangeNotAvailable on Deployment?
✔ Fix:

Check API key permissions (Spot & Margin trading enabled)
Test Binance API request on Streamlit Cloud:
python
Copy
Edit
import requests
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
response = requests.get(url)
print(response.status_code, response.text)
Ensure dependencies are installed in requirements.txt
Use a VPN if Binance is restricted in your region
👨‍💻 Developer
👤 [Your Name]
🔗 LinkedIn: Your LinkedIn Profile
📧 Email: your-email@example.com
🔗 GitHub: yourusername

