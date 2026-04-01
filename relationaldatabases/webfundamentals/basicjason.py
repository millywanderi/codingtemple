#!/usr/bin/env python3 

import json

# Parsing JSON Data
x =  '{"name": "Kylie", "age": 10, "school": "Precious Brooks"}'
y = json.loads(x)
print(y["school"])
