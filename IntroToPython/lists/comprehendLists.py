#!/usr/bin/env python3

# offers shorter syntax of the list
fruits = ["apple", "berries", "banana", "mango", "date"]
newfruits= []

for x in fruits:
    if "a" in x:
        newfruits.append(x)
print(newfruits)

# One can comprehend above using the following
fruits = ["apple", "berries", "banana", "mango", "date"]
newfruits = [x for x in fruits if "a" in x]
print(newfruits)

# condition
fruits = ["apple", "berries", "banana", "mango", "date"]
newfruits = [x for x in fruits if x != "banana"]
print(newfruits)

# iterate
newlist = [x for x in range(10)]
print(newlist)

# Use condition to iterate
newlist = [x for x in range(10) if x <= 5]
print(newlist)
