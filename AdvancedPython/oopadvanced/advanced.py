#!/usr/bin/env python3

"""
Example: E-commerce Product Class

Let’s take a common scenario—creating a Product class for an 
e-commerce platform. We want to use __repr__ to display useful 
debugging information for developers and __str__ to give users a clean
output.
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"


    def __str__(self):
        return f"{self.name}: ${self.price} (Quantity: {self.quantity})"

p = Product("Laptop", 999.99, 5)
print(repr(p))

print(p)

"""
Example: Managing a Fleet of Cars

Consider a Car class where the company wants to track the total number
of cars produced and also offer alternative ways to create cars, such
as importing car data from a CSV file. We’ll use class methods to 
manage these operations.
"""
class Car:
    total_cars = 0

    def __init__(self, model, year):
        self.model = model
        self.year = year
        Car.total_cars += 1


    @classmethod
    def from_csv(cls, csv_data):
        model, year = csv_data.split(",")
        return cls(model, int(year))


    @classmethod
    def total_produced(cls):
        return cls.total_cars


car1 = Car("Toyota Corolla", 2020)
car2 = Car.from_csv("Honda Accord,2018")

print(Car.total_produced())
