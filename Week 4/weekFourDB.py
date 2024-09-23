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
    print("This program converts measurements in cups to fluid ounces or gallons to liters.")
    print("For your reference the formulas are:")
    print("1 cup = 8 fluid ounces")
    print("1 gallon = 3.78541 liters")
    print()

# The cups_to_ounces function accepts a number of cups and displays the
# equivalent number of fluid ounces.
def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")

# The gallons_to_liters function accepts a number of gallons and displays the
# equivalent number of liters.
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    print("That converts to", liters, "liters.")

# The main function
def main():
    intro()
    
    try:
        choice = int(input("Enter 1 to convert cups to ounces or 2 to convert gallons to liters: "))
        
        if choice == 1:
            cups_needed = float(input("Enter the number of cups: "))
            # Convert cups to fluid ounces.
            cups_to_ounces(cups_needed)
        elif choice == 2:
            gallons_needed = float(input("Enter the number of gallons: "))
            # Convert gallons to liters.
            gallons_to_liters(gallons_needed)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            main()
    except ValueError:
        print("An exception occurred, try again by entering a valid number.")
        print()
        main()

# Call the main function.
main()

