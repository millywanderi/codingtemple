#!/usr/bin/env python3

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
