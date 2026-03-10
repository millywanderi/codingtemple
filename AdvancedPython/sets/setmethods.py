#!/usr/bin/env python3

# Membership Checks
names = {"Steve", "Millie", "Kylie", "Lyle"}
print("Kylie" in names)
print("Sue" in names)

# Adding Items to a Set
names = {"Steve", "Millie", "Kylie", "Lyle"}
names.add("Kinsley")
print(names)

# Subset and Superset Checks
num1 = {5, 6, 7}
num2 = {5, 6, 7, 8, 9}

print(num1.issubset(num2))
print(num2.issuperset(num1))
