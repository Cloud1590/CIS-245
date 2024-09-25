'''
file = open("example.txt", "r")

content = file.read()
print(content)

file.close()
'''

'''

file = open("example.txt", "w")

content = file.write("hello")
print(content)

file.close()
'''


'''
file = open("example.txt", "r")
line = file.readline()
print(line)
line = file.readline()
print(line)
file.close()
'''

'''
file = open("example.txt", "r")
content = file.read()
print(content)

print(content[0], content[1], content[2], content[3], content[4])
'''



'''
messsage = "Hello, this is content from a variable.\n"
file = open("example.txt", "w")
file.write(messsage)
message = "This is the second line of the file."
file.write(message)
file.close()
'''



# what does the \n do?
# The \n is an escape sequence that represents a newline character.
# When the \n is encountered in a string, it causes the text following it to be printed on a new line.
# In this case, the \n is used to insert a newline character between the two lines of text in the file.
# What is the difference between the "w" and "a" modes?
# The "w" mode is used to open a file for writing. If the file already exists, it will be overwritten.
# The "a" mode is used to open a file for appending. If the file already exists, new data will be added to the end of the file.

'''
message = "Hello, this is content from a variable.\n"
file = open("example.txt", "a")
file.write(message)
file.close()
'''

'''
file = open("example.txt", "r")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()
'''

#write a loop to write 1-1000 fo a file called "numbers.txt"
#wach number gets its own line

'''

file = open("numbers.txt", "w")
for i in range(1, 1001):
    file.write(str(i) + "\n")
file.close()

file = open("numbers.txt", "r")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()


file = open("example.txt", "r")
for line in file:
    print(line)
file.close()

'''

'''

Transactions = open("transactions.txt" , "r")
Account = open("account.txt" , "r")
total_transactions = 0
account_balance = 10000

for line in Transactions:
    total_transactions = total_transactions + int(line)
for line in Account:
    account_balance = int(line)

account_balance = account_balance - total_transactions
print("The account balance is: ", account_balance)

Transactions.close()
Account.close()
Account = open("account.txt" , "w")
Account.write(str(account_balance))
Account.close()

'''

'''
try:
    file = open("exmaple.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("The file was not found.")

'''

try:
    number = '10'
    number = number + 10

except TypeError:
    print("wrong data type.")

except:
    print("An exception occurred.")








# The open function is used to open a file. 
# The open function takes two arguments: the name of the file to open and the mode in which to open the file. 
# The mode can be "r" for read, "w" for write, or "a" for append. 
# The open function returns a file object that can be used to read from or write to the file.