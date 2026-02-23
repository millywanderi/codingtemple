#!/usr/bin/env python3
import random

"""
Design a program that will help someone decide between two activities 
based on the weather and mood.
"""
# Ask the user for the weather (sunny or raining) and their mood 
# (happy or tired)
weather = input("Select one option from (sunny or raining):" ).lower()
mood = input("Select one option from (happy or tired):" ).lower()

if weather == "sunny" and mood == "happy":
    print("Go for hike")
else:
    print("Relax indoors")

"""
Write a program where the user has to guess a secret number between 1
and 10. The program should provide feedback if the guess is too high 
or too low and congratulate the user if they guess correctly.
"""
secret_num = random.randint(1, 10)
guess_num = int(input("Guess a number between 1 and 10: ", ))
if guess_num == secret_num:
    print("Congratulations! You guessed the correct number.")
elif guess_num < secret_num:
    print("Too Low!")
else:
    print("Too High!")
