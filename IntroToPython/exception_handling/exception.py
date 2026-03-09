#!/usr/bin/env python3

import sys

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

# NameError
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something alse went wrong")

# else keyword to define a block of code to be executed if no errors 
#were raised
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# finally block, if specified, will be executed regardless if the try
# block raises an error or not
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Try to open and write to a file that is not writable
try:
    f = open("file.txt")
    try:
        f.write("Hey")
    except:
        print("Something went wrong when writing this file")
    finally:
        f.close()
except:
    print("Something went wrong when opening this file")

# Raise an error and stop the program if x is lower than 0
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if x is not an integer
x = "Millie"
if not type(x) is int:
    raise TypeError("Only integers allowed")
