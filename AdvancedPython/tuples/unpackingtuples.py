#!/usr/bin/env python3

# Packing is when you take multiple values and group them together into 
#a tuple.
personal_info = "Mary", 30, "Developer"
print(personal_info)

# Unpacking is when you take a tuple and assign its values to 
#individual variables
personal_info = ("Mary", 30, "Developer")
name, age, profession = personal_info
print(name)
print(age)
print(profession)
