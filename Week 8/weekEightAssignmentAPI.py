import yfinance as yf

# Create a dictionary of stock tickers (symbols)
stocks = {
    "AAPL": "Apple Inc.",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com Inc.",
    "TSLA": "Tesla Inc.",
    "MSFT": "Microsoft Corporation",
    "NFLX": "Netflix Inc.",
    "DIS": "The Walt Disney Company",
    "VZ": "Verizon Communications Inc.",
    "WMT": "Walmart Inc.",
    "JNJ": "Johnson & Johnson",
    "CAG": "Conagra Brands Inc."
}




# Ask the user to enter a ticker symbol and make it uppercase if not already
ticker = input("Enter a ticker symbol: ").upper()

# Check if the ticker is in the dictionary
try:
    x = yf.Ticker(ticker)
    stockData = (x.history(period="1d"))
    
    stocks[ticker] = stockData


    # Add the latest closing price to the dictionary value
    for ticker in stocks.keys():
        stock_info = yf.Ticker(ticker)
        current_price = stock_info.history(period="1d")['Close'][0]  # Fetch the latest closing price
        stocks[ticker] = {"name": stocks[ticker], "price": current_price}

except:
    print("Ticker symbol not found. Please try again.")
    

for ticker, data in stocks.items():
    print(f"{ticker}: {data}")


    # Add the latest closing price to the dictionary value
    for ticker in stocks.keys():
        stock_info = yf.Ticker(ticker)
        current_price = stock_info.history(period="1d")['Close'][0]  # Fetch the latest closing price
        stocks[ticker] = {"name": stocks[ticker], "price": current_price}

'''
    
for s in stocks:
    stock_info = yf.Ticker(s)
    current_price = stock_info.history(period="1d")['Close'][0]  # Fetch the latest closing price
    print(f"Ticker symbol: {s} ({stocks[s]})")
    print(f"Stock price: ${current_price:.2f}")
    
    
x = yf.Ticker("AAPL")
print(x.history(period="5d"))

'''

print (stocks)