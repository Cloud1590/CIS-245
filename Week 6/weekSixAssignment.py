import os
# Needed for clearing the terminal before displaying the results

# Clear the terminal before the user enters numbers
os.system('clear')

# Initialize an empty list to store the numbers
number_list = []

# Loop to get 20 numbers from the user
for n in range(20):
    while True:
        try:
            # Prompt the user to enter a number
            num = int(input("Enter number " + str(n + 1) + " of 20: "))
            break
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid number.")
    # Add the valid number to the list
    number_list.append(num)
number_list = []
for n in range(20):
    
    while True:
        try:
            num = int(input("Enter number " + str(n + 1) + " of 20: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    number_list.append(num)


# Clear the terminal before displaying the results
os.system('clear')

# Display the results
print("The numbers you entered are: \n")
print(str(number_list) + "\n")
print("• The lowest number in the list is:", min(number_list))
print("• The highest number in the list is:", max(number_list))
print("• The total of the numbers in the list is:", sum(number_list))
print("• The average of the numbers in the list is:", sum(number_list) / len(number_list))