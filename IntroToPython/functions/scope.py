#!/usr/bin/env python3

# A scope is a variable is only available from inside the region it is created
def my_function():
    x = 200
    print(x)
my_function()

# The local variable can be accessed from a function within the function
def my_function():
    x = 200
    def myinnerfunction():
        print(x)
    myinnerfunction()
my_function()
