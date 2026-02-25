#!/usr/bin/env python3

"""
In a for loop, the else clause is executed after the loop finishes its 
final iteration, that is, if no break occurred.
"""
for x in range(6):
    print(x)
else:
    print("Finally finished")

# searches for prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, '*', n // x)
            break
    else:
        print(n, "is a prime number")

# Break the loop when x is 3, and see what happens with the else block
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished")

# Print color of each fruit
color = ["red", "yellow", "blue"]
fruits = ["apple", "banana", "blueberries"]

for x in color:
    for y in fruits:
        print(x, y)
