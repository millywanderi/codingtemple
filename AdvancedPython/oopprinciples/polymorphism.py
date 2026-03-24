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

# Create a class called Vehicle and make Car, Boat, Plane child 
#classes of Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
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

# Polymorphism in a Social Media Platform
class User:
    def post_content(self):
        print("Posting generic content.")


class RegularUser(User):
    def post_content(self):
        print("Posting a photo as a regular user.")


class Influencer(User):
    def post_content(self):
        print("Posting a sponsored video as an influencer.")


class Brand(User):
    def post_content(self):
        print("Posting an ad as a brand.")


def publish_post(user):
    user.post_content()


default_user = User()
user1 = RegularUser()
user2 = Influencer()
user3 = Brand()

publish_post(default_user)
publish_post(user1)
publish_post(user2)
publish_post(user3)

# Python allows classes to inherit from more than one class, which
#is known as multiple inheritance
class Flyer:
    def fly(self):
        print("Flying Higher!")


class Swimmer:
    def swim(self):
        print("Swimming Fast!")


class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()
