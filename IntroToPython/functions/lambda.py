#!/usr/bin/env python3

"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have 
one expression
"""

# Add 10 to argument a, and return the result
x = lambda a : a + 10
print(x(5))

# Summarize argument a, b, and c and return the result
x = lambda a, b, c: a + b + c
print(x(1, 2, 3))

# make a function that always doubles the number you send in
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# make a function that always triples the number you send in
def myfunc(n):
    return lambda a : a * n
mytrippler = myfunc(3)
print(mytrippler(22))

# make increment 
def myfunct(n):
    return lambda a : a + n
myincreament = myfunc(6)
print(myincreament(4))

# Using Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda a : a * 2, numbers))
print(doubled)

# Using Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda a : a % 2 != 0, numbers))
print(odd_numbers)
