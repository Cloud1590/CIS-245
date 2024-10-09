# Define a string
my_string = "Hello, World!"

# Get the length of the string
length_of_string = len(my_string)

# Iterate through the string using a for loop
for char in range(length_of_string):
    print("Character at index " + str(char))


# now, access the 18th element in the string.
#print(my_string[17])

x = "I am the first string"
print(id(x))

x = x + " and I am the second string"
print(id(x))

x = "w" + x[1:]


# Next example

x = 1
print(id(x))

x = x + 2
print(id(x))

# Strings are immutable in Python
# String slicing

# Define a string
my_string = "Hello, World!"
first_five_chars = my_string[:5]
middle_chars = my_string[7:12]
print("original string: " + my_string)
print("First five characters:", first_five_chars)
print("Middle characters:", middle_chars)

# Testing, Searching and Manipulating Strings

main_string = "Hello, welcome to Python programming"
sub_string = "Python"

if sub_string in main_string:
    print("Substring found in the main string")
else:
    print("Substring not found in the main string")

#python is annoying because it is case sensitive



# Changing the weekTwoAssignment.py code to have error handling

''''
# Display welcome message to the console
print("Welcome to the Fiber-Cost Calculator!")

try:
    # Get the length (In Feet) of fiber needed from the user
    fiberLength = float(input("Enter the length of fiber cable needed in feet: "))

    # Assign the cost of fiber per foot to a variable
    fiberCost = 0.87

    # Calculate the total cost of fiber
    totalCost = fiberLength * fiberCost

    # Determine the cost of fiber based on the number of feet requested
    if fiberLength > 500:
        fiberCost = 0.50
        totalCost = fiberLength * fiberCost
    elif fiberLength > 250:
        fiberCost = 0.70
        totalCost = fiberLength * fiberCost
    elif fiberLength > 100:
        fiberCost = 0.80
        totalCost = fiberLength * fiberCost

    # Print the output
    print("SpeedForce Fiber")
    print(f"The total cost of fiber is ${totalCost:.2f}")

    # Print the cost of fiber per foot to confirm the correct cost is being used
    print(f"The cost of fiber per foot is ${fiberCost:.2f}")

except ValueError:
    print("Invalid input. Please enter a numeric value for the length of fiber cable.")

'''




# another example

# Define a string
my_string = " Hello, Python! "

print("Left trimmed string:", len(my_string))

left_trimmed = my_string.lstrip()
right_trimmed = my_string.rstrip()
print("Original string:", my_string)

print("Left trimmed string:", left_trimmed)
print("Right trimmed string:", right_trimmed)

print("Left trimmed string:", len(left_trimmed))
print("Left trimmed string:", len(right_trimmed))



ip_list = []

ip_list.append("User connected from IP address 194.163.1.100 at 10:15 AM")
ip_list.append("User connected from IP address 196.164.1.100 at 9:15 AM")
ip_list.append("User connected from IP address 192.168.1.100 at 8:00 AM")
ip_list.append("User connected from IP address 198.168.1.100 at 7:15 AM")
ip_list.append("User connected from IP address 195.167.1.100 at 11:15 AM")
ip_list.append("User connected from IP address 197.166.1.100 at 4:15 PM")
ip_list.append("User connected from IP address 198.167.1.100 at 1:15 AM")

ip_address = "192.168.1.100"

for x in ip_list:
    position = x.find(ip_address)
    
    if position != -1:
        print("IP address" + ip_address + " found in the string:")