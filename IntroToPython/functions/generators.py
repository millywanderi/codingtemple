#!/usr/bin/env python3

# Generators are functions that can pause and resume their execution

# A simple generator function
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)

# Generator that yields numbers
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(7):
    print(num)

# Generator for large sequences
def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# manually iterate through a generator using the next() function
def simple_gen():
    yield "Steve"
    yield "Millie"
    yield "Kylie"
    yield "Lyle"
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# List comprehension vs generator expression
# list comprehension - creates lists
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator comprehension - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Using a generator expression with sum
total = sum(x * x for x in range(10))
print(total)

# Generate 100 Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
gen = fibonacci()
for _ in range(100):
    print(next(gen))
