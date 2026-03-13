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

# The values in dictionary items can be of any data type
my_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 2008,
    "colors": ["red", "white", "black", "grey"]
}
print(my_dict)

# Print the data type of a dictionary
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2008
}
print(type(my_dict))

# Using the dict() method to make a dictionary
my_dict = dict(name = "Kylie", age = 10, city = "Nairobi")
print(my_dict)
