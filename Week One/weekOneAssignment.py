#Display welcome message to the console
print("Welcome to the Fiber-Cost Calculator!")

#Get the length (In Feet) of fiber needed from the user
fiberLength = input("Enter the length of fiber cable needed in feet: ")

#Assign the cost of fiber per foot to a variable
fiberCost = 0.87

#Calculate the total cost of fiber
totalCost = int(fiberLength) * fiberCost

#Display the company name and total cost of fiber to the console

print("SpeedForce Fiber")
print("The total cost of fiber is $" + str(totalCost))