# Write a program that captures a string containing a person’s first, middle, and last names, and then display their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.


# Initialize empty list
names = []

# Get string from user
names.append(input("Enter first name: "))
names.append(input("Enter middle name: "))
names.append(input("Enter last name: "))


# Capitalize the first letter of each name
names = [name.capitalize() for name in names]

#display output
print(names[0][0] + ". " + names[1][0] + ". " + names[2][0] + ".")