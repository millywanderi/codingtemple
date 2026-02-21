#!/usr/bin/env python3

# and - Returns True if both statements are true
x = 30
y = 20
z = 10
if x > y and z < x:
    print("Both conditions are true")

# or Returns True if one of the statements is true
x = 30
y = 20
z = 10
if x > y or x < z:
    print("At least one condition is true")

# not - Reverses the result, returns False if the result is true
x = 30
y = 200
if not x > y:
    print("x is not greater than y")


