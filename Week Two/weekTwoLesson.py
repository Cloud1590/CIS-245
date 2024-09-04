'''
cold = 42
if cold < 50:
    print("It is cold outside!")
else: 
    print("It is not cold outside!")
'''
# The above code is an example of an if else statement.



'''
print("Welcome to BU Grading Center!")
# Get the grade from the user
grade = int(input("Enter your grade: "))
if grade >10: 
    print("You passsed!")
else:
    print("You failed!")


print("Thank you for using BU Grading Center!")
'''



'''
Determine if someone qualifies for a loan based on two conditions:
    1. They must make at least $30,000 per year
    2. They must have been at their current job for at least two years
'''

# Get the annual salary from the user
annualSalary = float(input("Enter your annual salary: "))
# Get the years at current job from the user
yearsAtJob = int(input("Enter the number of years at your current job: "))
# Determine if the user qualifies for a loan
if annualSalary >= 30000 and yearsAtJob >= 2:
    print("Congratulations! You qualify for a loan!")
else:
    print("Sorry, you do not qualify for a loan.")

