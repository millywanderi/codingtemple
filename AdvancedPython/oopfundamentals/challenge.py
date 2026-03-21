#!/usr/bin/env python3

"""
Create a class called Person
Add an __init__ method that takes name and age as parameters
Add a method called greet that prints "Hello, my name is " followed by the name
Create an object p1 of the class with name "John" and age 36
Call the greet method on p1
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is " + self.name)
p1 = Person("John", 36)
p1.greet()

"""
Create a class called Dog
Add an __init__ method with parameters name and age, and store them as properties using self
Add a method called bark that prints the dog's name followed by " says Woof!"
Create an object d1 of the Dog class with name "Buddy" and age 3
Call the bark method on d1
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name + " saya Woof!")
d1 = Dog("Buddy", 3)
d1.bark()

"""
Create a class called Car
Add an __init__ method with a brand parameter, and store it as a property
Add a method called show that prints the brand
Create an object c1 of the Car class with brand "Ford"
Call the show method on c1
"""
class Car:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(self.brand)
c1 = Car("Ford")
c1.show()


"""
Engage & Apply: Mid Lesson Exercise
Exercise: Create a Person Class
Objective: Apply the concepts of classes, attributes, and instance methods.
Instructions:
Create a class named Person with:
Instance attributes name (string) and age (integer).
Add two instance methods:
greet(): This method should return a greeting message that includes the person's name.
have_birthday(): This method should increase the person's age by one 
and return a message that says, "Happy Birthday! You are now [age] years old."
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        return f"Hello, {self.name}!"


    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old"

person = Person("Kylie", 10)
print(person.greet())
print(person.have_birthday())


"""
Final Challenge
Challenge: Create a BankAccount Class
Objective: Reinforce the concepts of instance attributes, the __init__ method, and instance methods.
Instructions:
Create a class named BankAccount with the following:
Instance attributes:
account_holder (string): The name of the account holder.
balance (float): The current account balance, defaulting to 0.
Methods:
deposit(amount): Adds the given amount to the account balance and 
returns a message showing the new balance. withdraw(amount): Subtracts
the given amount from the balance if there are sufficient funds. 
Otherwise, it should return a message saying "Insufficient funds." 
If the withdrawal is successful, it should return the new balance.
get_balance(): Returns a message displaying the current account balance.
"""
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}.Your new balance is ${self.balance}"


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Your new balance is ${self.balance}"
        else:
            return f"Insufficient funds"

    def get_balance(self):
        return f"Your current balance is ${self.balance}"

account = BankAccount("Kylie", 1000)

print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))


"""
Create a class Student with an __init__ that takes name and grade, 
and stores them as properties
Create an object s1 with name "Anna" and grade "A"
Print the grade of s1
Change the grade of s1 to "B"
Print the updated grade
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
s1 = Student("Anna", "A")
print(s1.grade)
s1.grade = "B"
print(s1.grade)


"""
Create a class called Rectangle
Add an __init__ method with width and height, and store them as properties
Add a method called area that returns the width multiplied by the height
Create an object r1 with width 5 and height 3
Print the area of r1
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height

r1 = Rectangle(5, 3)
print(r1.area())
