#!/usr/bin/env python3

# break statement stops looping
fruits = ["apple", "banana", "mango"]
for i in fruits:
    print(i)
    if i == "banana":
        break

# break before the identified item
fruits = ["apple", "banana", "mango"]
for i in fruits:
    if i == "banana":
        break
    print(i)

# advanced breaking
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break

# Do not print banana
fruits = ["apple", "banana", "mango"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The continue statement continues with the next iteration of the loop
for x in range(2, 10):
    if x % 2 == 0:
        print(f"Found an even number {x}")
        continue
    print(f"Found an odd number {x}")
