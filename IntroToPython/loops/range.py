#!/usr/ bin/env python3

# range is used to iterate over sequence of numbers
for i in range(5):
    print(i)

# Iterate using the start parameter
for i in range(2, 7):
    print(i)

# Increment the sequence with 3
for i in range(2, 30, 3):
    print(i)

# Iterate a list
for i in list(range(5, 10)):
    print(i)

# Iterate using len() and range()
fruits = ["apple", "banana", "mango"]
for i in range(len(fruits)):
    print(i, fruits[i])
