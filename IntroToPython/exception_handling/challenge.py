#!/usr/bin/env python3

"""
Write a program that prompts the user for two numbers, then divides 
the first by the second. Handle the exceptions where the user enters 
invalid data (non-numeric) or tries to divide by zero.
"""
try:
    x = int(input("Enter your first number "))
    y = int(input("Enter your second number "))

    z = x / y
except ValueError:
    print("The value is not an integer or float")
except ZeroDivisionError:
    print("You cannot divide the number by zero")

"""
Write a try block that tries to print a variable x (which is not defined)
Write an except block that prints "An error occurred"
Write a finally block that prints "Execution complete"
"""
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("Execution complete")

"""
Create a program that simulates an ATM withdrawal process. The program should:

Allow the user to input an amount to withdraw.
Raise an exception if the input is invalid (non-numeric or negative).
Ensure that the withdrawal doesn’t exceed the account balance, 
raising an appropriate exception.
Always display the remaining balance, even if an error occurs.
"""
balance = 10000
try:
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount < 0:
        raise ValueError("Withdrawal cannot be negative number")
    if amount > balance:
        raise Exception("Insufficient funds")
    balance -= amount
    print("Withdrawal successful")
except ValueError:
    print("Invalid! Enter a valid number")
except Exception as e:
    print("Error:", e)
finally:
    print("The remaining balance:", balance)


