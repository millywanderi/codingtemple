#!/usr/bin/env python3

# Example of Public Attributes (BankAccount)
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

account = BankAccount("Jane", 1000)
print(account.account_holder)
account.balance += 500
print(account.balance)

# Example of Protected Attributes (BankAccount)
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance


    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def add_interest(self, interest_rate):
        self._balance += self._balance * interest_rate
savings = SavingsAccount("Bob", 2000)
savings.add_interest(0.05)
print(savings.get_balance())

# Create a private class property named __age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def get_age(self):
        return self.__age

p1 = Person("John", 12)
print(p1.get_age())

# Example of Private Attributes (Social Media Profile)
class SocialMediaProfile:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.__password = password


    def verify_password(self, input_password):
        if input_password == self.__password:
            return "Password Verified"
        else:
            return "Invalid Password"


    def get_email(self, input_password):
        if input_password == self.__password:
            return self.__email
        else:
            return "Access Denied"

profile = SocialMediaProfile("user123", "user@gmail.com", "securepassword")
print(profile.get_email("securepassword"))

# Use encapsulation to protect and validate data
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0


    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")


    def get_grade(self):
        return self.__grade


    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

student = Student("Carol")
student.set_grade(80)
print(student.get_grade())
print(student.get_status())
