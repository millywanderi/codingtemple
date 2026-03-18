#!/usr/bin/env python3

import re

# Split at each white-space character
txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)

#Split the string only at the first occurrencex
x = re.split(r"\s", txt, 1)
print(x)

"""
split a string based on various delimiters such as commas, semicolons
, spaces, periods, and hyphens.split a string based on various 
delimiters such as commas, semicolons, spaces, periods, and hyphens.
"""
txt = "Python,Regex;Splitting-Example. Fun, right?"
words = re.split(r"[,.;\s-]+", txt)
print(words)
