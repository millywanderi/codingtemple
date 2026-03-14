#!/usr/bin/env python3

# Make a copy of a dictionary with the copy() method
mydict = {
    "name": "Kylie",
    "age": 10,
    "city": "Nairobi"
}
thisdict = mydict.copy()
print(thisdict)

# Make a copy of a dictionary with the dict() function
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1960
}
mycar = dict(car)
print(mycar)
