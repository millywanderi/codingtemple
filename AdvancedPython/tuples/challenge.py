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

#mytuple.add("Mary")
#print(mytuple)


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


"""
Final Challenge: Tuple Mastery
Now that you’ve explored the basics, let’s put everything together!

Create a Tuple: Create a tuple with at least 6 elements. Feel free to
mix different data types like integers, strings, and floats.
Access and Print Elements: Access and print the third and fifth 
elements using indexing.
Slice the Tuple: Slice the tuple to extract elements from the second 
to the fifth position
Count Occurrences: Use the count() method to find how many times a 
specific value appears in your tuple.
Unpack the Tuple: Unpack the tuple into individual variables and 
print them.
Concatenate Tuples: Concatenate your tuple with another tuple and 
print the new tuple.
"""
mytuple = (1.1, "Mary", True, 30, "Developer", True)
print("Third element:", mytuple[2])
print("Fifth element:", mytuple[4])
print(mytuple[1:5])
print(mytuple.count(True))

a,b, c, d, e, f = mytuple
print(a, b, c, d, e, f)

newtuple = mytuple + (1.2, "Ann", 29, False)
print(newtuple)
