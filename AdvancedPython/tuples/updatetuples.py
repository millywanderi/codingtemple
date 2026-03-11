#!/usr/bin/env python3

# Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
print(tuple(y))

# Add Items
x = ("apple", "banana", "mango")
y = list(x)
y.append("orange")
print(tuple(y))

# Add tuple to a tuple
x = ("apple", "banana", "mango")
y = ("kiwi",)
x += y
print(x)
