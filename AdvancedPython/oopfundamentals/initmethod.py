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

# basic example to understand instance methods
class Car:
    def __init__(self, make, model, mileage=0):
        self.make = make
        self.model = model
        self.mileage = mileage

    
    # Instance method to display car information
    def display_info(self):
        return f"{self.make} {self.model}, Mileage: {self.mileage} miles"


    # Instance method to update the mileage
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total mileage is now {self.mileage} miles."
# Creating an instance of the Car class
mycar = Car("Toyota", "Corolla", 10000)
print(mycar.display_info())
print(mycar.drive(150))
