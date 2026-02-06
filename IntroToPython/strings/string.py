#!/usr/bin/env python3

# A string is a sequency of characters enclosed in '', "", or """"""

# Simple stings
name = "John"
print(name) # print John

greeting = 'Hello'
print(greeting) # prints hello

multi_line = '''My name is Kylie. I am 10 years old. I school at Good
Testimony Schools. I am at Grade 5.'''
print(multi_line)

# strings index/array starts at 0
name = "Kylie"
print(name[0]) # prints k
print(name[3]) # prints i

# Loop through a string
for m in "kylie":
    print(m)

# string length
name = "Kylie Kinsley"
print(len(name)) # output is 13

# Check string
txt = "I am going to the market"
if "going" in txt:
    print("Yes, 'going' is in txt")
else:
    print("No, 'going' is NOT in text")
