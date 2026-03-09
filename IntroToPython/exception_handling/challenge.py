#!/usr/bin/env python3

"""
Write a program that prompts the user for two numbers, then divides 
the first by the second. Handle the exceptions where the user enters 
invalid data (non-numeric) or tries to divide by zero.
"""
try:
    x = int(input("Enter your first number "))
    y = int(input("Enter your second number "))

    z = x / y
except ValueError:
    print("The value is not an integer or float")
except ZeroDivisionError:
    print("You cannot divide the number by zero")

"""
Write a try block that tries to print a variable x (which is not defined)
Write an except block that prints "An error occurred"
Write a finally block that prints "Execution complete"
"""
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("Execution complete")
