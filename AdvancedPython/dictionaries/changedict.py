#!/usr/bin/env python3

# change the value of a specific item by referring to its key name
my_dict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks"
}
my_dict["school"] = "Karamani Baptist"
print(my_dict)

# Update Dictionary
my_dict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks"
}
my_dict.update({"name": "Kinsley"})
print(my_dict)
