#!/usr/bin/env python3

# Accessing values by key
my_dict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks"
}
print(my_dict["school"])

# Get the value of the "model" key
my_dict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks"
}
print(my_dict.get("name"))
print(my_dict.get("age"))
