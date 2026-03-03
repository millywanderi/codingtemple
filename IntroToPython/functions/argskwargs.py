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

# A function that calculates the sum of any number of values
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

# Finding the maximum value
def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 7, 2, 9, 1))

# Using **kwargs to accept any number of keyword arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Lyle", lname = "Macharia")

# Accessing values from **kwargs
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
my_function(name = "Lyle", age = 7, city = "Nairobi")

# Using **kwargs with Regular Arguments
def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)
my_function("millie", age = 31, city = "Nairobi", hobby = "coding")

# Combining *args and **kwargs
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional Arguements:", args)
    print("Keyword Arguements:", kwargs)

my_function("User Info", "Millie", "Wanderi", age = 31, city = "Nairobi")

# Unpacking Lists with *
def my_function(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
results = my_function(*numbers)
print(results)
