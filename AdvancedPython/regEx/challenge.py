#!/usr/bin/env python3

import re

# extract all hashtags using a regex pattern
tweets = [
    "Loving the #sunset! So peaceful #nature #blessed"
    "Had a great day! #happy #friends #goodvibes"
    "Can't wait for the #weekend! #fun #relax"
]
tags = []
for tweet in tweets:
    tags.extend(re.findall(r"#\w+", tweet))
print(tags)
