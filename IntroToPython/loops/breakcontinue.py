#!/usr/bin/env python3

# break statement stops looping
fruits = ["apple", "banana", "mango"]
for i in fruits:
    print(i)
    if i == "banana":
        break

# break before the identified item
fruits = ["apple", "banana", "mango"]
for i in fruits:
    if i == "banana":
        break
    print(i)
