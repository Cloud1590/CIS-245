#Write a program that uses a while loop to determine how long it takes for an investment to double at a given interest rate. 
#The input will be an annualized interest rate and the initial investment amount. The output is the number of years it takes an investment to double.

investment = 10000
interest_rate = 0.10
w = 0

while investment < 20000:
    investment = investment + (investment * interest_rate)
    w += 1
print(w)
#What is the purpose of the variable w?
# the variable w is used to keep track of the number of years it takes for the investment to double
#What does that mean?
# it means that the variable w is incremented by 1 each time the investment is updated
