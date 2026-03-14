#!/usr/bin/env python3

# Print all key names in the dictionary, one by one
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1980
}
for x in car:
    print(x)
    print(car[x]) # Print all values in the dictionary, one by one

for x in car.values():
    print(x)
