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

# Sending a dictionary as an argument
def my_function(person):
    print("Name", person["name"])
    print("Age", person["age"])
my_person = {"name": "Steve", "age": 36}
my_function(my_person)

# Functions can return values using the return statement
def my_function(a, b):
    return a + b
result = my_function(10, 20)
print(result)

# Returning Different Data Types
def my_function():
    return ["Steve", "Millie", "Kylie", "Lyle"]
names = my_function()
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# A function that returns a tuple
def my_function():
    return (20, 30)
a, b = my_function()
print("a:", a)
print("b:", b)

# Positional-Only Arguments
def my_function(name, /):
    print("Hello", name)
my_function("Millie")

# Without the , / you are actually allowed to use keyword arguments 
# even if the function expects positional arguments
def my_function(name):
    print("Hello", name)
my_function(name = "Kylie")

# Keyword-Only Arguments
def my_function(*, name):
    print("Hello", name)
my_function(name = "Lyle")

# Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
    return a + b + c + d
result = my_function(2, 3, c = 4, d = 5)
print(result)
