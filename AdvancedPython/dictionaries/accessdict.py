#!/usr/bin/env python3

# Accessing values by key
my_dict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks"
}
print(my_dict["school"])

# Use get() to access the value of the key
my_dict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks"
}
print(my_dict.get("name"))
print(my_dict.get("age"))

# Add a new item to the original dictionary, and see that the keys 
#list gets updated as well
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)
car["color"] = "blue"
print(x)

# Get a list of the values
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.values())
