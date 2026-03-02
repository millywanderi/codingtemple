#!/usr/bin/env python3

# The *args parameter allows a function to accept any number of 
# positional arguments.
def my_function(*kids):
    print("My youngest kid is " + kids[1])
my_function("Kylie", "Lyle")
