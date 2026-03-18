#!/usr/bin/env python3

import re

# Do a search that will return a Match Object
txt = "The rain in Spain"
x = re.search(r"ai", txt)
print(x)
