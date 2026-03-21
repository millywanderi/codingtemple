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
