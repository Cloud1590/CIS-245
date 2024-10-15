# Create a program that includes a dictionary of stocks. 
# Your dictionary should include at least 10 ticker symbols. 
# The key should be the stock ticker symbol and the value should be the current price of the stock (the values can be fictional.) 
# Ask the user to enter a ticker symbol. Your program will search the dictionary for the ticker symbol and then print the ticker symbol and the stock price. 
# If the ticker symbol is not located, print a message indicating that the ticker symbol was not found.


# Create a dictionary of stocks
stocks = {
    "AAPL": 150.00,
    "GOOGL": 2500.00,
    "AMZN": 3500.00,
    "TSLA": 700.00,
    "MSFT": 300.00,
    "NFLX": 500.00,
    "DIS": 150.00,
    "VZ": 50.00,
    "WMT": 150.00,
    "JNJ": 150.00
}

# Ask the user to enter a ticker symbol, and make it uppercase if not already
ticker = input("Enter a ticker symbol: ").upper()

if ticker in stocks:
    print("Ticker symbol: ", ticker)
    print("Stock price: ", stocks[ticker])

else:
    print("Ticker symbol not found. Please try again.")

# What happens if you look for a ticker symbol that is not in the dictionary?
# If you look for a ticker symbol that is not in the dictionary, the program will print "Ticker symbol not found."

# What is a ticker symbol?
# A ticker symbol is a unique series of letters assigned to a security for trading purposes.
# Example: AAPL is the ticker symbol for Apple Inc.