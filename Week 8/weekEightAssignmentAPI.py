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
    "JNJ": "Johnson & Johnson"
}

# Ask the user to enter a ticker symbol and make it uppercase if not already
ticker = input("Enter a ticker symbol: ").upper()

# Check if the ticker is in the dictionary
if ticker in stocks:
    stock_info = yf.Ticker(ticker)
    current_price = stock_info.history(period="1d")['Close'][0]  # Fetch the latest closing price
    print(f"Ticker symbol: {ticker} ({stocks[ticker]})")
    print(f"Stock price: ${current_price:.2f}")
else:
    print("Ticker symbol not found. Please try again.")