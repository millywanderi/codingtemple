#!/usr/bin/env python3

import re

# Do a search that will return a Match Object
txt = "The rain in Spain"
x = re.search(r"ai", txt)
print(x)

# The regular expression looks for any words that starts with an 
#upper case "S"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
