#!/usr/bin/env python3

# simple list
fruits = ["apple", "mango", "banana"]
print(fruits)

# Lists allow duplicates
fruits = ["apple", "mango", "banana", "apple"]
print(fruits)

# Get the list length
fruits = ["apple", "mango", "banana"]
print(len(fruits))

# one can list items of various data types
list1 = ["apple", "mango", "banana"]
list2 = [10, 20, 30]
list3 = ["True", "False", "True"]
print(list1)
print(list2)
print(list3)

# One can mix different data types in one list
list1 = [23, "True", 3.0, "True"]
print(list1)

# Get the list data type
list1 = ["apple", "mango", "banana"]
list2 = [10, 20, 30]
list3 = ["True", "False", "True"]
print(type(list1))
print(type(list2))
print(type(list3))

# use list constructor to construct new list
newlist = list(("Steve", "Millicent", "Kylie", "Lyle"))
print(newlist)

"""
Define a list called "fruits" containing the following items: 
"apple", "banana", "cherry", and "date".
"""
fruits = ["apple", "banana", "cherry", "date"]

"""
Print the first item in the list
Print the last item using negative indexing.
"""
print(fruits[0])
print(fruits[-1])
