#!/usr/bin/env python3

"""
Create a function introduce_yourself that takes a name and favorite hobby. 
The function should print a greeting and mention the person's hobby.
"""
def introduce_yourself(name, hobby):
    print(f"Hello, {name}! Correct me if I'm wrong, but your favorite hobby is {hobby}.")
introduce_yourself("Kylie", "dancing")
introduce_yourself("Lyle", "swimming")

"""
Create a function called greet
Add a parameter called name to the function
Inside the function, print "Hello, " followed by the name parameter
Call the function with the argument "Emil"
"""
def greet(name):
    print("Hello", name)
greet("Emil")
