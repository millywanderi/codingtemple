#!/usr/bin/env python3

# A simple recursive function that counts down from 5
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown( n - 1)
countdown(5)

# Identifying base case and recursive case
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Find the 7th number in the Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))

# Recursion can be used to process lists by handling one element at a time
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

# Find the maximum value in a list
def find_max(num):
    if len(num) == 1:
        return num[0]
    else:
        max_rest_num = find_max(num[1:])
        return num[0] if num[0] > max_rest_num else max_rest_num
my_list = [ 2, 7, 18, 1, 5]
print(find_max(my_list))
