#while loop that displays the numbers 1-10
num = 1
while num <= 10:
    print(num)
    num += 1  

# Output: 1 2 3 4 5 6 7 8 9 10
#identify the initialization, comparison, and update expressions in the while loop
# initialization: num = 1
# comparison: num <= 10

x = 1

for x in 4, 5, 6, 7, 8, 9, 10:
    print(x)


for z in range(10):
    print(z)

for x in range(1, 11):
    print(x)

#write a program that prints the following output:
'''
3a
4a
5a
6a
7a
'''

for x in range(3, 8):
    print(str(x) + 'a')


for x in range(3, 8):
    print(str(x))

#"what the for loop is going on here?"

t = 1

if t % 2 == 0:
    print('str(t) is an even number')
else:
    print('str(t) is an odd number')

t = t + 1







for t in range(1, 11):
    if t % 2 == 0:
        print(str(t) + ' is an even number')
    else:
        print(str(t) + ' is an odd number')





my_name = 'Daniel'
for x in my_name:
    print(x)

#why doesn't it print D over and over again?
# because the for loop is iterating through each character in the string

my_name = 'Daniel'
for x in range(len(my_name)):
    print(my_name[x])

#what are the square brackets called?
# the square brackets are called index brackets
#what do they do?
# they are used to access the character at the specified index in the string
#what is the purpose of the square brackets in the print statement?
# the square brackets are used to access the character at the specified index in the string
#what does that mean?
# it means that the character at the specified index in the string is printed
#what is the purpose of the len function?
# the len function returns the length of the string
#what does that mean?
# it means that the number of characters in the string is returned
#what is the purpose of the range function?
# the range function generates a sequence of numbers
#what does that mean?
# it means that a sequence of numbers is generated


# ask if there's a difference between while loop and while true loop
# while loop: executes as long as the condition is true
# while true loop: executes indefinitely
# ask if there's a difference between while loop and for loop
# while loop: executes as long as the condition is true
# for loop: executes a specific number of times



#Input validation: Inspecting the input before it is processed by the program
#ask the user to enter a score
#validate the input to ensure that the score is not negative


while True:
    score = int(input('Enter a score: '))
    if score < 0:
        print('The score cannot be negative')
    else:
        break





while True:
    score = int(input('Enter a score: '))
    if score < 0 and score > 100:
        print('The score cannot be negative')
    else:
        break

#why won't this work?
#the condition should be an or condition instead of an and condition
#why
# because the score cannot be negative and greater than 100 at the same time
#what is the purpose of the break statement?
# the break statement is used to exit the loop
#what does that mean?
# it means that the loop is terminated and the program continues executing the next statement after the loop





#calculate interest of 10% on an investment of $10000

investment = 10000
interest_rate = 0.10
w = 0

while w < 1*2:
    investment = investment + (investment * interest_rate)
    w += 1
    print(investment)
#I don't understand what is happening here