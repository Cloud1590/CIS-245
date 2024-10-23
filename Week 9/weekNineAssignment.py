'''
Your program will then use the methods of the student class to accomplish the following:
Prompt the user for the first and last name of the student.
Create a student object by passing the first and last name to the __init__ method.
Create a loop that prompts the user for the following: The credits and grade for each course the student has taken.
Once the user ends the loop display the student’s cumulative GPA.


Create a student class that implements the following class diagram that will calculate and display student cumulative GPA: 

Student
Attributes:
First Name
Last Name
Grade Point
Credits
GPA
Methods:
__init__
CalculateGPA
GetGPA
'''

class Student:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.grade_points = 0
		self.credits = 0
		self.gpa = 0.0

	def calculate_gpa(self):
		if self.credits > 0:
			self.gpa = self.grade_points / self.credits
		else:
			self.gpa = 0.0

	def get_gpa(self):
		return self.gpa

# Prompt the user for the first and last name of the student
first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

# Create a student object
student = Student(first_name, last_name)

# Create a loop to prompt for credits and grades
while True:
	credits = input("Enter the number of credits for the course (or 'done' to finish): ")
	if credits.lower() == 'done':
		break
	grade = input("Enter the grade for the course: ")

	try:
		credits = float(credits)
		grade = float(grade)
	except ValueError:
		print("Invalid input. Please enter numeric values for credits and grade.")
		continue

	student.credits += credits
	student.grade_points += credits * grade

# Calculate and display the student's cumulative GPA
student.calculate_gpa()
print(f"{student.first_name} {student.last_name}'s cumulative GPA is: {student.get_gpa()}")


