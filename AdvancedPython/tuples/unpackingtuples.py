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

# When unpacking, if you're not interested in one or more values, you 
#can use an underscore _ as a placeholder to ignore those values
personal_info = ("Mary", 30, "Developer", "Louisville")
name, _, _, city = personal_info
print(name)
print(city)

# A function can return multiple values, packed into a tuple
def get_user_info():
    return "Mary", 30, "Developer", "Louisville"
name, age, profession, city = get_user_info()
print(city)

# Passing Multiple Values with Unpacking
def display_info(name, age, profession):
    print(f"{name} is {age} years old and work as a {profession}")

info_tuple = ("Mary", 30, "Developer")
display_info(*info_tuple)
