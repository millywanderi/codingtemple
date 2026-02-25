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
