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



x = 1
print(id(x))

x = x + 2
print(id(x))




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