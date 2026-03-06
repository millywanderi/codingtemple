#!/usr/bin/env python3

# Generators are functions that can pause and resume their execution

# A simple generator function
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)
