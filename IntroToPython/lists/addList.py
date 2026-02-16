#!/usr/bin/env python3

# Use append() to add an item at the end of list
names = ["Steve", "Millie", "Kylie"]
names.append("Lyle")
print(names)

# use insert() to add an item at the specific index
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.insert(2, "Kinsley")
print(names)

# use extend() to extend current list
myList = [1, 2, 3]
names = ["boy", "girl", "man"]
myList.extend(names)
print(myList)

# use extend() to add iterable object
myList = [1, 2, 3]
myTuple = ("boy", "girl", "man")
myList.extend(myTuple)
