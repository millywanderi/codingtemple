#!/usr/bin/env python3

# The *args parameter allows a function to accept any number of 
# positional arguments.
def my_function(*kids):
    print("My youngest kid is " + kids[1])
my_function("Kylie", "Lyle")

# Accessing individual arguments from *args
def my_function(*args):
    print("Type: ", type(args))
    print("I have two children, namely ", args[0] + " and", args[1])
my_function("Kylie", "Lyle")

# Using *args with Regular Arguments
def my_function(greetings, *names):
    for name in names:
        print(greetings, name)
my_function("Hello", "Kylie", "Lyle")
