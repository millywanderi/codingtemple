#!/usr/bin/env python3

# Simple __init__ method example
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating instances of Car class
car1 = Car("Toyota", "Corolla", 2009)
car2 = Car("Honda", "Civic", 2010)

# Accessing instance attributes
print(car1.make, car1.model, car1.year)
print(car2.make, car2.model, car2.year)

# Set a default value for the age parameter
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
p1 = Person("Millie")
p2 = Person("Kylie", 10)

print(p1.name, p1.age)
print(p2.name, p2.age)
