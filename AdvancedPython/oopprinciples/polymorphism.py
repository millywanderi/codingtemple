#!/usr/bin/env python3

"""
Polymorphism allows different types of objects to be treated as if 
they are instances of the same class.
"""

# Different classes with the same method
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def move(self):
        print("Fly!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    x.move()
