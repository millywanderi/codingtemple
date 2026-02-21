#!/usr/bin/env python3

x = 30
y = 20

if x > y: print("x is greater than y")

# short hand if or else
x = 30
y = 20
print("X") if x > y else print("Y")

# assign a value using short hand
x = 30
y = 20
bigger = x if x > y else y
print("Bigger is", bigger)
