#!/usr/bin/env python3

# it catches anything which isn't caught by the preceding conditions
a = 30
b = 20

if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")

# else without elif
a = 30
b = 20
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# else provides default when other condions are not met
x = 9

if x % 2 == 0:
    print("x is an even number")
else:
    print("x is not an odd number")

# combine if, elif, else conditions
temperature = 21

if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cold outside")
else:
    print("It's freezing outside")

# else as a fallback
username = "Millie"

if len(username) > 0:
    print(f"Welcome {username}")
else:
    print("Error, can't find the username")
