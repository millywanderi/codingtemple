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
