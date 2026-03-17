#!/usr/bin/env python3

import re

# Search the string to see if it starts with "The" and ends with "Spain"
txt = "The girl in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Yes! We have a match")
else:
    print("No match")
