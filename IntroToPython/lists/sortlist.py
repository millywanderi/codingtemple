#!/usr/bin/env python3

# sort alphabetically
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.sort()
print(names)

# sort numerically
numbers = [23, 45, -7, 3.14]
numbers.sort()
print(numbers)

# sort descending
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.sort(reverse = True)
print(names)

numbers = [23, 45, -7, 3.14]
numbers.sort(reverse = True)
print(numbers)

# Sort the list based on how close the number is to 50
def myfunc(x):
    return abs(x - 50)

numbers = [75, 50, 22, 83, 100]
numbers.sort(key = myfunc)
print(numbers)

# sort is case sensitive
names = ["Steve", "millie", "Kylie", "lyle"]
names.sort(key = str.lower)
print(names)

# reverse()
names = ["Steve", "Millie", "Kylie", "Lyle"]
names.reverse()
print(names)
