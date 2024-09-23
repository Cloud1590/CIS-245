# Example code that converts cups to fluid ounces.

def main():
    #display intro screen.
    intro()

    try:
    #get the number of cups.
        cups_needed = float(input("Enter the number of cups: "))
    
    #convert cups to fluid ounces.
        cups_to_ounces(cups_needed)

       except:
        print("An exception occurred, try again by entering a number.")
        print() 
        main()

    # The intro function displays an introductory screen.
def intro():
    print("This program converts measurements in cups to fluid ounces.")
    print("For your reference the formula is:")
    print("1 cup = 8 fluid ounces")
    print()

    # The cups_to_ounces function accepts a number of cups and displays the
    # equivalent number of fluid ounces.
def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")

# Call the main function.
main()

