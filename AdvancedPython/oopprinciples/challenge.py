#!/usr/bin/env python3

"""
Create a class ScoreBoard
Add an __init__ with a score parameter and store it as a private attribute
Add a method called get_score that returns the private score
Create an object s1 with a score of 0
Print the score of s1
"""
class ScoreBoard:
    def __init__(self, score):
        self.__score = score


    def get_score(self):
        return self.__score

s1 = ScoreBoard(0)
print(s1.get_score())
