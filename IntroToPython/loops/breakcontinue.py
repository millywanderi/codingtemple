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
