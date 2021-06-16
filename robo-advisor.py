import os
import requests
import pandas as pd
from datetime import date
from dotenv import load_dotenv

# "https://www.alphavantage.co/query?function=CRYPTO_RATING&symbol=BTC&apikey="
# symbol = input("Please enter a stock ticker").upper()
Alpha_API_Key = os.getenv("Alpha_API_Key")
func = "TIME_SERIES_DAILY_ADJUSTED"

while True:
    symbol = input("please enter a stock ticker").upper()
    if symbol.isalpha() and len(symbol) > 1 and len(symbol) < 7:
        break
    else:
        print("Please enter a valid ticker")

base_url = f"https://www.alphavantage.co/query?function={func}&symbol={symbol}&apikey={Alpha_API_Key}"
x = requests.get(base_url)
df = pd.DataFrame(x)
print(df)
# str = x.text
# splitted = str.split("Time Series Daily")
# print(splitted)
# broken = splitted[0].split('\n')
# print(broken[1])
# # Make a request["Time Series Daily"]
