# Review this in class

names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint"]

for x in names:
    print(x)

for x in range(len(names)):
    print(names[x])
    
for x in names:
    for y in x:
        print(y)
        
for x in names:
    for y in range(len(x)):
        print(x[y])
        
        
        
        
# Define a dictionary

people_and_ages ={
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "Diana": 28,
}


# Print the dictionary

print("People in the dictionary: ")

for x in people_and_ages.keys():
    print(x)


# Print the ages in the dictionary

print("Ages in the dictionary: ")

for x in people_and_ages.values():
    print(x)
    

# Print the key value pairs in the dictionary

print("Key value pairs in the dictionary: ")

for x in people_and_ages.items():
    print(x)




#add new person to the dictionary

people_and_ages["Eve"] = 35

# If the key exists, the value is updated

print(people_and_ages)

del people_and_ages["Eve"]

print(people_and_ages)




# Find the age of a specific person

Person = "Bob"

if Person in people_and_ages:
    print(people_and_ages[Person])
else:
    print("Person not found")
    
# What happens if you look for a person that is not in the dictionary?

Person = "Sam"

if Person in people_and_ages:
    print(people_and_ages[Person])    
else:
    print("Person not found")
    
    
# Now do the same with Try/Except

Person = "Sam"

try:
    print(people_and_ages[Person])
except:
    print("Person not found")
    

print("----------------------")

Age = people_and_ages.get("Sam")
print("Age: ", Age)

if Age == None:
    print("Person not found")





Age = people_and_ages.get("Sam")

if Age == None:
    print("Person not found")
else:
    print("Age: ", Age)



names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint"]

for x in range(len(names)):
    for y in range(len(names[x])):
        print(names[x][y])




Age = people_and_ages.get("Sam", "Person not found")


if Age == "Person not found":
    print("Person not found")
else:
    print("Age: ", Age)
