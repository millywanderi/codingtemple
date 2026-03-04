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

# Using the @changecase decorator on two functions
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunc():
    return "Hello Sally"

@changecase
def myotherfunc():
    return "I am speed"

print(myfunc())
print(myotherfunc())

# Functions with arguments can also be decorated
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def myfunc(nam):
    return "Hello " + nam
print(myfunc("Nelly"))
