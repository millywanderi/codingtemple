#!/usr/bin/env python3

num = 17
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is postive and odd")
else:
    print("The number is negative")

# Request user to insert 0-20 number
x = int(input("Enter a number between 0 and 20:", ))
if x > 10:
    print("Is above 10.")
    if x > 20:
        print("Is above 20.")
    else:
        print("but not above 100")
else:
    print("Is below 10.")

# Checking multiple conditions with nesting
age = 28
has_licence = True

if age >= 18:
    if has_licence:
        print("You can drive.")
    else:
        print("You need a licence.")
else:
    print("You are too young to drive.")

# Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

# Nested If vs Logical Operators
temperature = 25
is_sunny = True

if temperature > 22 and is_sunny:
    print("Perfect weather for swimming")
else:
    print("Too cold")
