#!/usr/bin/env python3

from abc import ABC, abstractmethod

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

# Polymorphism with Game Characters
class Character:
    @abstractmethod
    def attack(self):
        print("This method should be overridden by subclasses.")


class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword!")


class Mage(Character):
    def attack(self):
        print("Mage casts fireball!")


class Archer(Character):
    print("Archer shoots an arrow!")

def perform_attack(character):
    character.attack()

warrior = Warrior()
mage = Mage()
archer = Archer()

perform_attack(warrior)
perform_attack(mage)
perform_attack(archer)
