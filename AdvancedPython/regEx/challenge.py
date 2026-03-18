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


"""
Create a variable txt with the value "The rain in Spain"
Search for "Spain" in txt and store the result in x
Print the position (span) of the match
"""
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


"""
Final Challenge (End of Lesson Exercise)
Task: You are tasked with creating a simple email validation script 
that accepts a list of emails and checks if they are valid based 
on a regex pattern.
"""
emails = [
    "correct@email.com",
    "right@email.com",
    "dontcallme@email.org"
    "incorrect-email-at-example.com"
]
pattern = r"[\w.-]+@[\w-]+\.[a-z]{2,3}"

for email in emails:
    if re.search(pattern, email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")
