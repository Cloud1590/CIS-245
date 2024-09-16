# Input from the user
initial_investment = float(input("Enter the initial investment amount: $"))
annual_rate = float(input("Enter the annualized interest rate (in %): "))

years = 0
current_amount = initial_investment
target_amount = initial_investment * 2

# Loop until the investment doubles
while current_amount < target_amount:
    current_amount += current_amount * (annual_rate / 100)  # Applying interest
    years += 1  # Counting the years

# Print the result directly using string concatenation
print("It will take " + str(years) + " years for your investment to double.")