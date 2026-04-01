#!/usr/bin/env python3 

import json

# Parsing JSON Data
x =  '{"name": "Kylie", "age": 10, "school": "Precious Brooks"}'
y = json.loads(x)
print(y["school"])

# Use loads() to parse json to python
person = '''
{
    "name": "Millie",
    "age": 26,
    "skills": ["Python", "Data Analysis"]
}
'''

data = json.loads(person)

name = data["name"]
skills = data["skills"]

print(f"Name: {name}, Skills: {skills}")

# Serializing (Converting) Python Data to JSON
x = {
        "name": "Lyle",
        "age": 7,
        "city": "Nairobi"
}
y = json.dumps(x)
print(y)

# Convert Python dictionary to JSON string
person_json = {
    "name": "John",
    "age": 30,
    "is_student": False
}
data = json.dumps(person_json)
print(data)

# Convert Python objects into JSON strings, and print the values
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
