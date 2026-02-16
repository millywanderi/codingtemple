#!/usr/bin/env python3

# change the second item of the list
names = ["Steve", "Millie", "Kylie", "Lyle"]
names[1] = "Millicent"
print(names) # prints ['Steve', 'Millicent', 'Kylie', 'Lyle']

# change the range of item values
names = ["Steve", "Millie", "Kylie", "Lyle"]
names[1:3] = ["Millicent", "Kinsley"]
print(names)

# change the second item by replacing it with two values
names = ["Steve", "Millie", "Kylie", "Lyle"]
names[1:2] = ["Millicent", "Kinsley"]
print(names)
