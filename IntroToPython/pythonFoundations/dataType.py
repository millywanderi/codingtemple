#!/usr/bin/env python3

# String
x = "love"
print(type(x))

# Int
x = 3
print(type(x))

# Float
x = 3.0
print(type(x))

# Complex
x = 1j
print(type(x))

# List
names = ["Millicent", "Kylie", "Lyle"]
print(type(names))

# tuple
colors = ("beige", "pink", "blue")
print(type(colors))

# range
x = range(8)
print(x)
print(list(x)) # convert to list to display the contents

# dict
x = {"name" : "kylie", "age" : 10}
print(x)
print(type(x))

# set
x = {"yellow", "green", "purple"}
print(x)
print(type(x))

# frozenset - It removes duplicates
x = frozenset({"yellow", "green", "purple", "yellow"})
print(x)
print(type(x))

# bool
x = True
print(x)
print(type(x))

# bytes
x = b"Kylie"
print(x)
print(type(x))
