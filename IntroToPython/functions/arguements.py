#!/usr/bin/env python3

# Function that takes both parameters and value
def greet(name):
    print(f"Hello, {name}!")
greet("Sam")

# A function with one argument
def my_name(first_name):
    print(first_name + " Wanderi")
my_name("Winnie")
my_name("Irene")
my_name("Millie")

# A function with three arguments
def my_name(fname, mname, lname):
    print(fname + ' '+  mname + ' ' + lname)
my_name("Millicent", "Nyambura", "Wanderi")

# Default Parameter Values
def my_country(country = "Kenya"):
    print("I am from", country)
my_country("Rwanda")
my_country()
my_country("USA")

# creates a function that can be called with fewer arguments than it is defined to allow
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nope"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("Invalid user response")
        print(reminder)
