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
file = open("example.txt", "r")
line = file.readline()
print(line)
line = file.readline()
print(line)
file.close()

# The open function is used to open a file. 
# The open function takes two arguments: the name of the file to open and the mode in which to open the file. 
# The mode can be "r" for read, "w" for write, or "a" for append. 
# The open function returns a file object that can be used to read from or write to the file.