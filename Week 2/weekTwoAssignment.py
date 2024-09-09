'''
Building on the program you developed in Module 1, you will implement if statements for this assignment. In Module 1, you calculated the total cost of fiber cable installation by multiplying the number of feet by $.87. 
For this assignment, you will evaluate a bulk discount. Modify your program from Module 1 with the following steps:
Display a welcome message for your program.
Capture the number of feet of fiber optic to be installed from the user.
Evaluate the total cost based on the number of feet requested as described below.
If the user purchases more than 100 feet, they are charged $.80 per foot.
If the user purchases more than 250 feet, they will be charged $.70 per foot.
If they purchase more than 500 feet, they will be charged $.50 per foot.
Display the calculated information including the number of feet requested and the company name.
'''

# Display welcome message to the console
print("Welcome to the Fiber-Cost Calculator!")

# Get the length (In Feet) of fiber needed from the user
fiberLength = input("Enter the length of fiber cable needed in feet: ")

# Assign the cost of fiber per foot to a variable
fiberCost = 0.87

# Calculate the total cost of fiber
totalCost = float(fiberLength) * fiberCost

# Determine the cost of fiber based on the number of feet requested
if float(fiberLength) > 500:
    fiberCost = 0.50
    totalCost = float(fiberLength) * fiberCost
elif float(fiberLength) > 250:
    fiberCost = 0.70
    totalCost = float(fiberLength) * fiberCost
elif float(fiberLength) > 100:
    fiberCost = 0.80
    totalCost = float(fiberLength) * fiberCost

# Print the output
print("SpeedForce Fiber")
print(f"The total cost of fiber is ${totalCost:.2f}")

#print the cost of fiber per foot to confirm the correct cost is being used
print(f"The cost of fiber per foot is ${fiberCost:.2f}")