#!/usr/bin/env python3

# offers shorter syntax of the list
fruits = ["apple", "berries", "banana", "mango", "date"]
newfruits= []

for x in fruits:
    if "a" in x:
        newfruits.append(x)
print(newfruits)
