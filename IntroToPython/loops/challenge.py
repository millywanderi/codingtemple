#!/usr/bin/env python3

"""
Create a list called fruits with: "apple", "banana", "cherry"
Write a for loop that prints each item in fruits
Use break to stop the loop when the item is "banana"
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

"""
Create a variable i with the value 0
Write a while loop that runs as long as i is less than 6
Inside the loop: increment i by 1
If i equals 3, use continue to skip that iteration
print i
"""
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

"""
Write a Python program that prints all the even numbers between 1 and 
20 using a while loop.
"""
x = 1
while x <= 20:
    if x % 2 == 0:
        print(x)
    x += 1
