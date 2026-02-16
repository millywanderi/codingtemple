#!/usr/bin/env python3

# use remove() to remove a specific item
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.remove("Kylie")
print(names)

# remove the first occurrence of the item if it appears twice
names = ["Steve", "Kylie", "Millie", "Kylie", "Lyle"]
names.remove("Kylie")
print(names)

# remove item from specified index
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.pop(1)
print(names)
