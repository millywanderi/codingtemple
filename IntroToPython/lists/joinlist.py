#!/usr/bin/env python3

# use + to join lists
list1 = [20, 21, 22]
list2 = [23, 24, 25]
list3 = list1 + list2
print(list3)

# join list by appending
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

# use extend to join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
