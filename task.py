import requests
import matplotlib.pyplot as plt
import pandas as pd

# API Configuration
API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
PARAMS = {"vs_currency": "usd", "days": "7", "interval": "daily"}

# Fetch Data from API
response = requests.get(API_URL, params=PARAMS)
if response.status_code == 200:
    try:
        data = response.json()
        if "prices" in data:
            timestamps = [entry[0] for entry in data["prices"]]
            prices = [entry[1] for entry in data["prices"]]
            
            df = pd.DataFrame({"Time": pd.to_datetime(timestamps, unit='ms'), "Price (USD)": prices})
            
            plt.figure(figsize=(10, 5))
            plt.plot(df["Time"], df["Price (USD)"], marker='o', linestyle='-')
            plt.xlabel("Time")
            plt.ylabel("Price (USD)")
            plt.title("Bitcoin Price Trend (Last 7 Days)")
            plt.xticks(rotation=45)
            plt.grid()
            plt.show()
        else:
            print("Error: 'prices' key not found in API response.")
    except ValueError:
        print("Error: Failed to parse JSON response.")
else:
    print(f"Error: API request failed with status code {response.status_code}.")
