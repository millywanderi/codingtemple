#!/usr/bin/env python3

"""
Create a class called Person
Add an __init__ method that takes name and age as parameters
Add a method called greet that prints "Hello, my name is " followed by the name
Create an object p1 of the class with name "John" and age 36
Call the greet method on p1
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is " + self.name)
p1 = Person("John", 36)
p1.greet()

"""
Create a class called Dog
Add an __init__ method with parameters name and age, and store them as properties using self
Add a method called bark that prints the dog's name followed by " says Woof!"
Create an object d1 of the Dog class with name "Buddy" and age 3
Call the bark method on d1
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name + " saya Woof!")
d1 = Dog("Buddy", 3)
d1.bark()
