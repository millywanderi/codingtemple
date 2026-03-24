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
