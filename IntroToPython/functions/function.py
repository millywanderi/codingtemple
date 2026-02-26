#!/usr/bin/env python3

# A function is a block of organized, reusable code
def greet():
    print("Hello, welcome to my world!")
greet()

# Why use functions. Lets see code without and with a function
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# Same code with a function
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# A function that returns a value
def greetings():
    return "Hello, welcome to my world!"
message = greetings()
print(message)

# return directly
def name():
    return "My name is Millie"
print(name())
