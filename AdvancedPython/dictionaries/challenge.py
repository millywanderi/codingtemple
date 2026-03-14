#!/usr/bin/env python3

"""
Engage & Apply: Create a Dictionary 
Exercise: Create a dictionary that represents a book. Include keys 
like title, author, year, and genre. Write code to add a new key for 
publisher, and modify the value for year.

In this exercise, we use dictionaries to model more complex data. By adding new keys🔑 and modifying existing ones, students get a hands-on understanding of dictionary dynamics.
"""
book = {
    "title": "The River Between",
    "author": "Ngugi wa Thiong'o",
    "year": 2012,
    "genre": "Set book"
}

book.update({"publisher": "KLB"})
book.update({"year": 2020})
print(book)
