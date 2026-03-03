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

# A variable created outside of a function is global and can be used by anyone
x = 200
def myfunct():
    print(x)
myfunct()
print(x)

# The function will print the local x, and then the code will print the global x
x = 200
def myfunct():
    x = 150
    print(x)
myfunct()
print(x)

# If you use the global keyword, the variable belongs to the global scope
def myfunc():
    global x
    x = 200
myfunc()
print(x)

# To change the value of a global variable inside a function, 
# refer to the variable by using the global keyword
x = 200
def myfunc():
    global x
    x = 300
myfunc()
print(x)
