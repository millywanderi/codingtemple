#!/usr/bin/env python3

# Union: Combines all unique items from two sets
set1 = {"Steve", "Millie", "Kylie"}
set2 = {"Kinsley", "Lyle"}

grand_gather = set1.union(set2)
print(grand_gather)

# Intersection: Returns only the items both sets have in common
set1 = {"Steve", "Millie", "Kylie", "Lyle"}
set2 = {"Steve", "Millie","Jane", "Albert"}

mutual_friends = set1.intersection(set2)
print(mutual_friends)

# Difference: Returns the items found in one set but not the other
set1 = {"Steve", "Millie", "Kylie"}
set2 = {"Ann", "Job", "Kylie"}

exclusive_guests = set1.difference(set2)
print(exclusive_guests)

# Symmetric Difference: Returns the items that are unique to each set
#(not shared by both)
set1 = {"Steve", "Millie", "Kylie"}
set2 = {"Ann", "Job", "Kylie"}

unique_guests = set1.symmetric_difference(set2)
print(unique_guests)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
