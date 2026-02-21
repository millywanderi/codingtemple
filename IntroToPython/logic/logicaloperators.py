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

# Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
