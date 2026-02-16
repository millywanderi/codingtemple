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

# use pop to remove the last item
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.pop()
print(names)

# del() can also be used to delete the specified index item
names = ["Steve", "Millie", "Kylie", "Lyle"]
del names[0]
print(names)

# use clear() to empty the list
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.clear()
print(names)
