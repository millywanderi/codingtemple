#!/usr/bin/env python3

"""
Create a list called colors with the values "red", "green", "blue"
Print the first item in the list
Change the second item to "yellow"
Add "purple" to the end of the list
Remove "red" from the list
Print the list
"""
colors = ["red", "green", "blue"]
print(colors[0])
colors[1] = "yellow"
colors.append("purple")
colors.remove("red")
print(colors)

"""
Create a program that asks the user for their top 3 favorite books, 
stores them in a list, and prints the list in a sorted order.
"""

# Initialize an Empty List and prompt the User for Input.
favoritebooks = []
for i in range(3):
    book = input(f"Enter your favorite book {i + 1}: ")
    favoritebooks.append(book)
favoritebooks.sort()
print(favoritebooks)
