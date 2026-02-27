#!/usr/bin/env python3

def my_child(child, name):
    print("I have a", child)
    print("My", child + "'s name is", name)
my_child(child = "daughter", name = "Kylie")

# Positional Arguments
def my_function(animal, name):
    print("I have an", animal)
    print("My", animal + "'s name is", name)
my_function("cat", "kiti")

# Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
my_function("cat", name = "kiti", age = 2)

# Passing Different Data Types
def my_function(names):
    for name in names:
        print(name)
my_names = ["Steve", "Millie", "Kylie", "Lyle"]
my_function(my_names)
