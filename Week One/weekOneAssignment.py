#Display welcome message to the console
print("Welcome to the Fiber-Cost Calculator!")

#Get the length (In Feet) of fiber needed from the user
fiberLength = input("Enter the length of fiber cable needed in feet: ")

#Assign the cost of fiber per foot to a variable
fiberCost = 0.87

#Calculate the total cost of fiber
totalCost = float(fiberLength) * fiberCost



#print("SpeedForce Fiber")
#print("The total cost of fiber is $" + str(totalCost))

'''
the above commented code is what I had before I found out about the f-string formatting
to fix the output to two decimal places in some cases where the dollar amount
does not have two decimal places. 

example of this:
total length of fiber = 50
output would be 43.5 instead of 43.50

I think this should be addressed briefly during class at some point. 
I helped Michael with this issue because he ran into it as well.
'''

# Formatting the output string to include two decimal places
print("SpeedForce Fiber")
print(f"The total cost of fiber is ${totalCost:.2f}")




