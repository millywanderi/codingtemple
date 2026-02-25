#!/usr/bin/env python3

"""
In a for loop, the else clause is executed after the loop finishes its 
final iteration, that is, if no break occurred.
"""
for x in range(6):
    print(x)
else:
    print("Finally finished")
