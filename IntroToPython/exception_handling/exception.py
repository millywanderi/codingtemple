#!/usr/bin/env python3

"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of 
the try- and except blocks.
"""
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")

# Catching Multiple Exceptions in one block
try:
    a = int(input("Enter your favorite number: "))
    b = 10 / a
except (ValueError, ZeroDivisionError) as e:
    print(f"An error has occured: {e}")
