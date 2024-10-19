import pandas as pd
import requests
import yfinance as yf

# Function to get the list of S&P 500 tickers from Wikipedia
def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = requests.get(url)
    sp500_list = pd.read_html(response.text)[0]  # Read the first table on the page
    tickers = sp500_list['Symbol'].values.tolist()
    return tickers

# Fetch the list of S&P 500 tickers
sp500_tickers = get_sp500_tickers()

# Display the first 10 tickers
print("First 10 S&P 500 tickers:", sp500_tickers[:10])

# Now you can use these tickers to get stock data
def get_stock_price(ticker):
    stock_info = yf.Ticker(ticker)
    history = stock_info.history(period="1d")
    
    # Check if valid data is returned
    if not history.empty:
        latest_price = history['Close'][0]
        return latest_price
    else:
        return None

# Ask the user to enter a ticker symbol
ticker = input("Enter a ticker symbol from the S&P 500: ").upper()

# Check if the ticker is in the list of S&P 500 tickers
if ticker in sp500_tickers:
    stock_price = get_stock_price(ticker)
    if stock_price:
        print(f"Ticker symbol: {ticker}")
        print(f"Stock price: ${stock_price:.2f}")
    else:
        print(f"Could not fetch stock price for {ticker}.")
else:
    print(f"Ticker symbol {ticker} not found in the S&P 500.")