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

# Inheritance in a Video Game Character System
# parent class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def move(self):
        print(f"{self.name} is moving!")


    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")


# subclass: warrior
class Warrior(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor


    def use_shield(self):
        print(f"{self.name} blocks the attack with a shield!")


# Subclass: mage
class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana


    def cast_spell(self):
        print(f"{self.name} casts a powerful spell!")

# create instances
warrior = Warrior("Conan", 100, 20, "Iron Armor")
mage = Mage("Gandalf", 80, 25, 100)

# call methods
warrior.move()
warrior.attack()
warrior.use_shield()

mage.move()
mage.attack()
mage.cast_spell()

# modify our video game Character example so that the attack() method 
#behaves differently for Warriors and Mages
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")


class Warrior(Character):
    def attack(self):
        print(f"{self.name} slashes with a sword, dealing with {self.attack_power} damage!")


class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a fireball, dealing {self.attack_power} damage!")

warrior = Warrior("Conan", 100, 20)
mage = Mage("Gandalf", 80, 25)

warrior.attack()
mage.attack()
