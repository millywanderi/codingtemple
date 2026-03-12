#!/usr/bin/env python3

"""
Tuple Exploration
Let’s try a quick exercise to engage with tuples and understand their behavior!

Create a Tuple: Create a tuple containing at least 4 different data
types, such as an integer, string, float, and boolean.
Access and Print Elements: Access and print the first and last
elements of your tuple.
Attempt to Modify the Tuple: Try modifying one element of the tuple
and observe the error. This will help you understand the immutability
of tuples.
"""
mytuple = (1, "Tom", True, 3.14)
print("First element:", mytuple[0])
print("Last element:", mytuple[-1])

mytuple.add("Mary")
print(mytuple)


"""
Test your understanding of creating, accessing, and unpacking tuples
Create a tuple called fruits with the values "apple", "banana", "cherry"
Print the second item in the tuple
Print the number of items using len()
Unpack the tuple into three variables a, b, c
Print the variable b
"""
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(len(fruits))

a, b, c = fruits
print(b)
