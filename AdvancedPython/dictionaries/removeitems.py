#!/usr/bin/env python3

# The pop() method removes the item with the specified key name
mydict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks",
    "brother": "Lyle"
}
mydict.pop("brother")
print(mydict)

# The popitem() method removes the last inserted item
mydict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks",
    "brother": "Lyle"
}
mydict.popitem()
print(mydict)

# The del keyword removes the item with the specified key name
mydict = {
    "name": "Kylie",
    "age": 10,
    "school": "Precious Brooks",
    "brother": "Lyle"
}
del mydict["school"]
print(mydict)

# The clear() method empties the dictionary
mydict = {
    "name": "Kylie",
    "age": 10,
    "city": "Nairobi"
}
mydict.clear()
print(mydict)
