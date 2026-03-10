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
