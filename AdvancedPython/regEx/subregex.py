#!/usr/bin/env python3

import re

# Replace every white-space character with the number 9
txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)
