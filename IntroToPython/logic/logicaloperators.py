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

# Using Parentheses for Clarity
age = 12
is_adult = False
is_home = True
if (age > 9 and is_adult) or is_home:
    print("You are a pre-teen")

# User authentication check
email = "mnw@gmail.com"
password = "mnw"
is_verified = True
if email and password and is_verified:
    print("Login successful")
else:
    print("Wrong email/password")

# Range checking with logical operators
score = 70

if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")
