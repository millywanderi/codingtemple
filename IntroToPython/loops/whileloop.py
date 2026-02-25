#!/usr/bin/env python3

# can execute a set of statements as long as a condition is true
x = 5
while x < 10:
    print(x)
    x += 1

# With the break statement we can stop the loop even if the while 
# condition is true
x = 5
while x < 10:
    print(x)
    if x == 7:
        break
    print(x)
    x += 1

# The continue Statement
x = 5
while x < 10:
    x += 1
    if x == 7:
        continue
    print(x)

# The else Statement
x = 5
while x < 10:
    print(x)
    x += 1
else:
    print("x is no longer less than 10")
