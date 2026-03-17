#!/usr/bin/env python3

import re

# Search the string to see if it starts with "The" and ends with "Spain"
txt = "The girl in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Yes! We have a match")
else:
    print("No match")

# The findall() function returns a list containing all matches
txt = "My name is Millie, and I like coding and reading"
ands = re.findall("and", txt)
print(ands)
print(len(ands))

# Return an empty list if no match was found
txt = "My name is Millicent, and I come from Kenya"
x = re.findall("Uganda", txt)
print(x)
