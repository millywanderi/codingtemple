#!/usr/bin/env python3

# A for loop is used for iterating over a sequence
fruits = ["apple", "banana", "Mango"]
for x in fruits:
    print(x)

# Looping through a string
fruit = "banana"
for x in fruit:
    print(x)

# Measure some strings
fruit = ["apple", "banana", "Mango"]
for x in fruits:
    print(x, len(x))

# Create a sample collection
users = {"Steve": "active", "Millie": "inactive", "Kylie": "active"}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
