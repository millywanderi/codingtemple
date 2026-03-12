#!/usr/bin/env python3

# Packing is when you take multiple values and group them together into 
#a tuple.
personal_info = "Mary", 30, "Developer"
print(personal_info)

# Unpacking is when you take a tuple and assign its values to 
#individual variables
personal_info = ("Mary", 30, "Developer")
name, age, profession = personal_info
print(name)
print(age)
print(profession)

# If the number of variables is less than the number of values, you 
#can add an * to the variable name and the values will be assigned to
#the variable as a list
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
red, yellow, *orange = fruits
print(red)
print(yellow)
print(orange)

# capture values from thefront to end of the tuple
numbers = (1, 2, 3, 4, 5)
first, *rest, last = numbers
print(first)
print(rest)
print(last)

# Add a list of values the "tropic" variable
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
red, *tropic, green = fruits
print(red)
print(tropic)
print(green)
