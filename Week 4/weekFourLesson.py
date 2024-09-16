# Functions!

#int() - converts a string to an integer
#float() - converts a string to a float
#str() - converts a number to a string
#input() - gets input from the user
#Print() - prints to the console
#input() - gets input from the user

# Functions are a way to organize code into reusable blocks.
# Functions are defined using the def keyword, followed by the function name and parentheses.
# def function_name(parameters):


def add_two_numbers(one, two):
    return one + two

for one in range(1, 10):
    two = one * 2
    # add two numbers
    sum = add_two_numbers(one, two)
    print(sum)

# Functions can take parameters, which are values that are passed to the function when it is called.


# Functions are given names. The name of a function is used to call the function and pass it parameters.
def put_that_thing_back_where_it_came_from_or_so_help_me():
    print("So help me!")
    print("https://www.youtube.com/watch?v=tqaHBfBSSuc")

put_that_thing_back_where_it_came_from_or_so_help_me()

x = "Hello"
y = "World"


def concatenate_strings(string_one, string_two):
    x = string_one + " " + string_two
    return x

print(concatenate_strings("Hello", "World"))

#or

z = concatenate_strings(x, y)
print(z)

def yoda_speak(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

print(yoda_speak("Hello World"))


# Functions can return values using the return keyword. 
# The return keyword is followed by the value that the function should return.
# The return keyword can be used to return any value, including numbers, strings, lists, and other data types.



def print_2(one, two):
    return (one, two)

def main():
    q = print_2("Hello", "World!")
    print(q)

if __name__ == "__main__":
    main()

# what in the if loop does this do?
# The if __name__ == "__main__": line is used to check if the script is being run as the main program.
# If the script is being run as the main program, the code inside the if block is executed.
# what does "__" mean?
# The __name__ variable is a special variable in Python that contains the name of the current module.
# When a Python script is run, the __name__ variable is set to "__main__" if the script is being run as the main program.
# If the script is being imported as a module, the __name__ variable is set to the name of the module.
