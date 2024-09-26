'''Create a program that performs file-processing activities. The following video provides an overview of the requirements and some helpful hints for completing your assignment: File Processing - Homework (Bellevue University, 2022).

While discussed in the video, the requirements for the program are also listed below.

Prompt the user for the file name.
Prompt the user for their name.
Prompt the user for their street address.
Prompt the user for their phone number.
Write the username, street address, and phone number to a comma-separated line in the file that your user typed in Step 1.
Once the data has been written to the file your program should read the file and display the contents.'''

def main():
    file_name = input("Enter the name of the file: ")
    name = input("Enter your name: ")
    address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")

    file = open(file_name, "w")
    file.write(name + ", " + address + ", " + phone_number + "\n")
    file.close()

    file = open(file_name, "r")
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()
    file.close()
    