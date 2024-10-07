# Initialize an empty list to store the numbers
number_list = []

# Loop to get 20 numbers from the user
for n in range(20):
    num = int(input("Enter number " + str(n + 1) + " of 20: "))
    number_list.append(num)

# Display the results
print("• The lowest number in the list is:", min(number_list))
print("• The highest number in the list is:", max(number_list))
print("• The total of the numbers in the list is:", sum(number_list))
print("• The average of the numbers in the list is:", sum(number_list) / len(number_list))

# Alternatively...

min = min(number_list)
max = max(number_list)
total = sum(number_list)
average = total / len(number_list)

print("• The lowest number in the list is:", min)
print("• The highest number in the list is:", max)
print("• The total of the numbers in the list is:", total)
print("• The average of the numbers in the list is:", average)
# The code snippet above is a simplified version of the code from weekSixAssignment.py.
# It gets 20 numbers from the user, calculates the minimum, maximum, total, and average of the numbers, and then displays the results.
# The code does not clear the terminal before displaying the results, unlike the original code.
# Additionally, the code uses variables to store the minimum, maximum, total, and average values, making it easier to reference these values in the print statements.
# Overall, the code snippet is more concise and straightforward compared to the original code.