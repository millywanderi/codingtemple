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
