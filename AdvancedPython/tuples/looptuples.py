#!usr/bin/env python3

# Iterate through the items and print the values
fruits = ("apple", "banana", "mango")
for i in fruits:
    print(i)

# Loop Through the Index Numbers
fruits = ("apple", "banana", "mango")
for i in range(len(fruits)):
    print(fruits[i])

# Print all items, using a while loop to go through all the index numbers
fruits = ("apple", "banana", "mango")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
