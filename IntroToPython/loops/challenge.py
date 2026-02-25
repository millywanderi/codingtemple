#!/usr/bin/env python3

"""
Create a list called fruits with: "apple", "banana", "cherry"
Write a for loop that prints each item in fruits
Use break to stop the loop when the item is "banana"
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
