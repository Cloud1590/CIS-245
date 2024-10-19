# Create a program that includes a dictionary of stocks. 
# Your dictionary should include at least 10 ticker symbols. 
# The key should be the stock ticker symbol and the value should be the current price of the stock (the values can be fictional.) 
# Ask the user to enter a ticker symbol. Your program will search the dictionary for the ticker symbol and then print the ticker symbol and the stock price. 
# If the ticker symbol is not located, print a message indicating that the ticker symbol was not found.

# Now making it more dynamic by using the yfinance library to get the stock price of the ticker symbol entered by the user.

# Install yfinance library
# Run this command in your terminal
# pip install yfinance

import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period="1d")
    if not stock_info.empty:
        return stock_info['Close'].iloc[-1]
    else:
        return None

# Ask the user to enter a ticker symbol, and make it uppercase if not already
ticker = input("Enter a ticker symbol: ").upper()

price = get_stock_price(ticker)
if price is not None:
    print(f"Ticker symbol: {ticker}, Stock price: ${price:.2f}")
else:
    print("Ticker symbol not found.")