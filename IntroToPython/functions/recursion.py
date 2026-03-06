#!/usr/bin/env python3

# A simple recursive function that counts down from 5
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown( n - 1)
countdown(5)

# Identifying base case and recursive case
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)
print(factorial(5))
