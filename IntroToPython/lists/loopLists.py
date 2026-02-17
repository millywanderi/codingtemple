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

# Getting the index in a loop with enumerate()
fruits = ["mango", "banana", "apple", "berry"]
for index, item in enumerate(fruits):
    print(f"index: {index} - item: {item}")

# Loop in Multiple Lists with zip()
fruits = ["mango", "banana", "apple", "berry"]
price = [30, 10, 25, 50]

for item, amount in zip(fruits, price):
    print(f"The {item} costs ${amount}")
