'''
Your program will then use the methods of the student class to accomplish the following:
Prompt the user for the first and last name of the student.
Create a student object by passing the first and last name to the __init__ method.
Create a loop that prompts the user for the following: The credits and grade for each course the student has taken.
Once the user ends the loop display the student’s cumulative GPA.
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

# Create a student object by passing the first and last name to the __init__ method

student = Student(first_name, last_name)

# Create a loop that prompts the user for the following: The credits and grade for each course the student has taken

while True:
	credits = input("Enter the credits for the course (or 'done' to finish): ")
	if credits == 'done':
		break
	grade = input("Enter the grade for the course: ")
	student.grade_points += float(credits) * float(grade)
	student.credits += float(credits)
 
# Once the user ends the loop display the student’s cumulative GPA

student.calculate_gpa()
print(f"Student: {student.first_name} {student.last_name}")
print(f"Cumulative GPA: {student.get_gpa():.2f}")

# Output:

# Enter the student's first name: John
# Enter the student's last name: Smith
# Enter the credits for the course (or 'done' to finish): 3
# Enter the grade for the course: 4.0
# Enter the credits for the course (or 'done' to finish): 4
# Enter the grade for the course: 3.5
# Enter the credits for the course (or 'done' to finish): 3
# Enter the grade for the course: 3.0
# Enter the credits for the course (or 'done' to finish): done
# Student: John Smith
# Cumulative GPA: 3.42




