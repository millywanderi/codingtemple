#!/usr/bin/env python3

# print all items one by one
fruits = ["mango", "banana", "apple"]
for x in fruits:
    print(x)

# print all items by referring to their index number
fruits = ["mango", "banana", "apple"]
for x in range(len(fruits)):
    print(fruits[x])

# Print all items, using a while loop to go through all the index numbers
fruits = ["mango", "banana", "apple"]
x = 0
while x < len(fruits):
    print(fruits[x])
    x = x + 1

# Looping Using List Comprehension
fruits = ["mango", "banana", "apple"]
[print(x) for x in fruits]
