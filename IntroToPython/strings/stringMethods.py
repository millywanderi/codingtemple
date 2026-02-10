#!/usr/bin/env python3
import random

# Python built-in methods upper and lower case
name = "Kylie Kinsley"
print(name.upper())

# Print lowercase
name = "Kylie Kinsley"
print(name.lower())

# strip() removes whitespaces from the beginning to te end
name = "Kylie Kinsley "
print(name.strip())

# replace() used for replacing string
name = "Kylie Kinsley"
print(name.replace("K", "L"))

# split() returns a list where the text between the specified separator becomes the list items
a = "Hello, World!"
b = a.split(",")
print(b)

# join() joins elements of a list into strings
words = ['My', 'name', 'is', 'Kylie', 'Kinsley']
sentence = " ".join(words)
print(sentence)

# startswith or endswith 
sentence = "My name is Kylie Kinsley"
print(sentence.startswith("My"))
print(sentence.startswith("my"))
print(sentence.endswith("Kinsley"))
print(sentence.endswith("Kylie"))

"""
Use string methods to:

* Convert it to uppercase.
* Remove any leading or trailing whitespace.
* Replace a word with another word of your choice.
* Split it into a list of words.
"""
my_string = '            Coding temple is the best bootcamp ever!      '
print(my_string.upper())
print(my_string.strip())
print(my_string.replace("temple", "temp"))
print(my_string.split())

"""
Final Challenge: Build a text-based name generator that combines 
random first and last names using string manipulation.
"""
first_names = ["Steve", "Millicent", "Kylie", "Lyle"]
last_names = ["Njogu", "Nyambura", "Wanjiku", "Macharia"]

first = random.choice(first_names)
last = random.choice(last_names)

full_name = f"{first} {last}"
print("Your generated name is:", full_name)
