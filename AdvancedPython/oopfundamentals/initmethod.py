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
print(car1.make)
print(car1.model)
print(car1.year)

print(car2.make)
print(car2.model)
print(car2.year)
