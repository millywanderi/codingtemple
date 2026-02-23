#!/usr/bin/env python3

num = 17
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is postive and odd")
else:
    print("The number is negative")

x = int(input("Enter a number between 0 and 20:", ))
if x > 10:
    print("Is above 10.")
    if x > 20:
        print("Is above 20.")
    else:
        print("but not above 100")
else:
    print("Is negative")
