#!/usr/bin/env python3

# A basic decorator that uppercases the return value of the decorated function
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def my_func():
    return "Hello Sally"
print(my_func())
