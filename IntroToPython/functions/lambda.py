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
