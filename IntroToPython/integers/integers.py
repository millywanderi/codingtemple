#!/usr/bin/env python3

# Integer presentation
a = 3 # positive integer
b = -3 # negative integer
c = 0 # zero integer

# arithmetic
x = 20
y = 10
print(x + y) # output is 30
print(x - y) # output is 10
print(x * y) # output is 200
print(x / y) # output is 2.0 because it gives a float
print(x // y) # output is 2 as it rounds off to the nearest whole number

# Calculate the total cost of the following items. Then, apply a 10% 
# discount and display the final amount.
milk = 5
eggs = 3
coffee = 10
total_cost = milk + eggs + coffee
discount = 10/100 * total_cost
final_amount = total_cost - discount
print(f"The Total Cost: ${total_cost}")
print(f"Final Amount after 10% discount: ${final_amount}")

# Exponentiation and Powers
x = 2 ** 3
print(x)

# Use pow()
x = 2
y = 3
print(pow(x,y))

# abs() function
x = -10
print(abs(x)) # output is 10

# round() function
x = 3.14
y = 3.57
print(round(x))
print(round(y))

# convert string into integer
x = "153"
print(int(x))

x = 153
print(str(x)) # it will print 153 but the class type is str

# modulus %
x = 7
y = 4
print(x % y)
