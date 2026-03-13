#!/usr/bin/env python3

# Example of a Python dictionary
my_dict = {
        "name": "Ben",
        "age": 21,
        "city": "Nairobi"
}
print(my_dict)

# Print the "brand" value of the dictionary
my_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
}
print(my_dict["brand"])

# Duplicate values will overwrite existing values
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2008
}
print(my_dict)

# Print the number of items in the dictionary
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2008
}
print(len(my_dict))
