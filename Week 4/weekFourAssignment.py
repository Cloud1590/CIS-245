'''Write a program that uses a function to convert kilometers to kilometers.
Your program should prompt the user for the number of kilometers driven, then call a function that converts kilometers to kilometers.
The program should then display the total kilometers and kilometers.'''

# The main function
def main():
    intro()
    
    try:
        miles_needed = float(input("Enter the number of miles: "))
        # Convert miles to kilometers.
        miles_to_kilometers(miles_needed)
    except ValueError:
        print("An exception occurred, try again by entering a valid number.")
        print()
        main()

# The intro function displays an introductory screen.
def intro():
    print("This program converts distance in miles to kilometers")
    print("For your reference the formulas are:")
    print("1 mile = 1.60934 kilometers")
    print()

# The miles_to_kilometers function accepts a number of miles and displays the equivalent number of kilometers.
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    print("That converts to", kilometers, "kilometers.")


# The main function
def main():
    intro()
    
    try:
        miles_needed = float(input("Enter the number of miles: "))
        # Convert miles to kilometers.
        miles_to_kilometers(miles_needed)
    except ValueError:
        print("An exception occurred, try again by entering a valid number.")
        print()
        main()

# Call the main function.
main()