'''Write a program that uses a function to convert miles to kilometers.
Your program should prompt the user for the number of miles driven, then call a function that converts miles to kilometers.
The program should then display the total miles and kilometers.'''
#no f strings
def miles_to_kilometers(miles):
    return miles * 1.60934

miles = float(input("Enter the number of miles driven: "))
kilometers = miles_to_kilometers(miles)

print("You drove", miles, "miles.")
print("That is", kilometers, "kilometers")


def stinky():
    print("I'm stinky!")
    print("https://www.youtube.com/watch?v=9bZkp7q19f0")

z = 0

def printTwo(one):
        x = one + 1
        return x
def printOne(one):
        x = one + 1
        return x

print(printOne(1))
print(printTwo(1))



