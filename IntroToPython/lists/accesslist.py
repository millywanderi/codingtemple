#!/usr/bin/env python3

fruits = ["apple", "mango", "banana", "banana", "cherry", "orange"]
print(fruits[1]) # output mango

# Access negative index
fruits = ["apple", "mango", "banana", "banana", "cherry", "orange"]
print(fruits[-1]) # output orange
print(fruits[-3]) # output banana

# slice a list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist1 = list1[1:4]
print(sublist1) # output [2, 3, 4]
print(list1[:4]) # [1, 2, 3, 4]

