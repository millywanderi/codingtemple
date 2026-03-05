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

# Secure the function with *args and **kwargs arguments
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase
def myfunc(nam):
    return "Hello " + nam
print(myfunc("Jerry"))

# A decorator factory that takes an argument and transforms the casing 
#based on the argument value.
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase(1)
def myfunc():
    return "Hello Peter"
print(myfunc())

# One decorator for upper case, and one for adding a greeting
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase
@addgreeting
def myfunc():
    return "Millie"
print(myfunc())

# A function's name can be returned with the __name__ attribute
def myfunction():
    return "Have a blessed day"
print(myfunction.__name__)
