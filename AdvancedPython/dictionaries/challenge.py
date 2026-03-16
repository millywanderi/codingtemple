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


"""
Create a dictionary called car with the keys "brand", "model", "year"
and values "Ford", "Mustang", 2024
Print the value of the "model" key
Add a new key "color" with the value "red"
Remove the "brand" key using pop()
Print the dictionary
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2024
}
print(car["model"])
car["color"] = "red"
car.pop("brand")
print(car)


"""
Final Challenge: Student Grade Program
Challenge: Write a program that takes a dictionary of students and 
their grades, then prints each student's name and whether they passed
or failed (consider passing as a grade ≥ 50).

This challenge aims to reinforce iteration through a dictionary and 
using conditional logic to determine outcomes based on data stored 
within.
"""
students = {
    "Ann": 60,
    "John": 34,
    "Stacy": 53,
    "Kimberly": 50
}
for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")
