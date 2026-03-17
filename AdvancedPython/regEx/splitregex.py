#!/usr/bin/env python3

import re

# Split at each white-space character
txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)
