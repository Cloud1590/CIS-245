#import os

# arrays

temp = []
temp.append(34)
temp.append(78)

for x in temp:
    print(x)
    
for x in range(len(temp)):
    print(temp[x])
    


'''

# list can have multiple data types

my_list = []
my_list.append("The correct answer is ")
my_list.append("80")

for x in my_list:
    print(x)
    
    
# using the range()

for x in range(2):
    print(x)

'''


'''

my_list = []
my_list.append("The correct answer is ")
my_list.append("80")

my_second_list = []
my_second_list.append("On the test")

x = my_list + my_second_list
print(x)
print(len(x))
print(x [0:2])

'''

# Customer claims product purchased did not arrive. first thing needed to be determined is if the product purchased the product. 

customer_name = input("Enter customer name: ")
product_purchased = input("Enter product purchased: ")

my_products = []  # empty list

try:
    with open(customer_name + ".txt", "r") as file:
        for x in file:
            my_products.append(x.strip())
except FileNotFoundError:
    print("Customer file not found.")

if product_purchased in my_products:
    print("Product purchased")
    
else:
    print("Product not purchased")
    
# could we do this without a file? - no. 
# coukd we do this without a list? - yes.

# use a dictionary instead

'''

my_products = {"product1": "laptop", "product2": "tablet", "product3": "phone"}

if product_purchased in my_products.values():
    print("Product purchased")
    
else:
    print("Product not purchased")

'''

