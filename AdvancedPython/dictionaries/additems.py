#!/usr/bin/env python3

# Adding an item to the dictionary is done by using a new index key 
#and assigning a value to it
my_dict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks"
}
my_dict["brother"] = "Lyle"
print(my_dict)

# Use update() to add an item to the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1970
}
car.update({"color": "blue"})
print(car)
