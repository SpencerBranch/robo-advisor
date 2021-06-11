import os
import requests
from dotenv import load_dotenv

# "https://www.alphavantage.co/query?function=CRYPTO_RATING&symbol=BTC&apikey="
symbol = "MSFT"
Alpha_API_Key = os.getenv("Alpha_API_Key")
func = "TIME_SERIES_DAILY_ADJUSTED"

base_url = f"https://www.alphavantage.co/query?function={func}&symbol={symbol}&apikey={Alpha_API_Key}"
x = requests.get(base_url)
print(x.text)

# Make a request
