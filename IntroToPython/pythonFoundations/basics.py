#!/usr/bin/env python3

# Create a program that takes your name, age, and favorite color
# as an input and prints them out.
name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favorite color: ")

print(f"{name}, {age}, {color}")

# Build a program that asks the user to input their exam score and then prints a message.
# Outputs should be as follows:

#    "Excellent" if the score is greater than 90.
#    "Good" if the score is between 70 and 90.
#    "Needs Improvement" if the score is below 70.

score = int(input("Enter your exam score: "))
if (score > 90):
    print("Excellent")
elif (score < 90 and score > 70):
    print("Good")
else:
    print("Needs Improvement")
