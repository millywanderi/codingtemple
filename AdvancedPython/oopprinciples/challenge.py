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


"""
Create a class called FitnessTracker with the following attributes:
Public Attribute: user_name (string) representing the name of the user.
Private Attribute: __steps (integer) representing the number of steps
the user has taken. Initialize this to 0.
Private Attribute: __calories_burned (float) representing the total 
calories burned. Initialize this to 0.0.
Add the following methods:
add_steps(steps): Increases the number of steps by the value provided.
get_steps(): Returns the current number of steps.
add_calories(calories): Increases the calories burned by the value provided.
get_calories_burned(): Returns the total calories burned.
reset_tracker(): Resets both steps and calories to their initial 
values (0 and 0.0).
Create an instance of FitnessTracker, track a few workouts by adding 
steps and calories, and then display the user’s progress.
"""
class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.__steps = 0
        self.__calories_burned = 0.0

    def add_steps(self, steps):
        if steps > 0:
            self.__steps += steps
            return f"{steps} added. Total steps: {self.__steps}"
        else:
            print("Steps must be positive.")


    def get_steps(self):
        return self.__steps


    def add_calories(self, calories):
        if calories > 0:
            self.__calories_burned += calories
            return f"{calories} calories burned. Total calories burned: {self.__calories_burned}"
        else:
            print("Calories must be positive.")


    def get_calories_burned(self):
        return self.__calories_burned

    
    def reset_tracker(self):
        self.__steps = 0
        self.__calories_burned = 0.0
        print("Tracker reset to 0 steps and 0.0 calories burned.")

tracker = FitnessTracker("Mercy")
tracker.add_steps(5000)
tracker.add_calories(300)

print(f"steps: {tracker.get_steps()}")
print(f"calories: {tracker.get_calories_burned()}")
tracker.reset_tracker()
