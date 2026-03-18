#!/usr/bin/env python3

import re

# The regular expression looks for any words that starts with an 
#upper case "S"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
