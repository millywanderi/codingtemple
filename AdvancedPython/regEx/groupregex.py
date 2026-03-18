#!/usr/bin/env python3

import re

# The regular expression looks for any words that starts with an 
#upper case "S"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# Capturing Parts of a Phone Number
number = "123-456"
pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, number)
if thematch:
    print(f"Group 1: {thematch.group(1)}")
    print(f"Group 2: {thematch.group(2)}")
