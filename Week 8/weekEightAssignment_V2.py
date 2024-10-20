import yfinance as yf

# Ask the user to enter a ticker symbol
ticker = input("Enter a ticker symbol: ").upper()

# Fetch the stock data using yfinance
stock = yf.Ticker(ticker)
stock_info = stock.history(period="1d")

# Check if the stock data is available
if not stock_info.empty:
    # Get the closing price of the stock
    closing_price = stock_info['Close'].iloc[0]
    print(f"The closing price of {ticker} is {closing_price}")
else:
    print(f"No data found for ticker symbol {ticker}")
