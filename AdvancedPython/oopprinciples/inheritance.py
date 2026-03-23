#!/usr/bin/env python3

"""
Inheritance allows us to define a class that inherits all the 
methods and properties from another class.
"""

# Create a class named Person, with firstname and lastname properties,
#and a printname method
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def printname(self):
        print(self.fname, self.lname)

p1 = Person("Lyle", "Macharia")
print(p1.printname())
