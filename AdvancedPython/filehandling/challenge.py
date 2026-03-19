#!/usr/bin/env python3

"""
Task: Create a simple Python program that:

Allows the user to add favorite foods to a list.
Stores the data in a file.
Lets the user view or remove items from the list.
"""
def write_foods(food):
    with open("foods.txt", "w") as file:
        for food in foods:
            file.write(food + "\n")

def read_foods():
    food_list = []
    with open("foods.txt", "r") as file:
        for line in file:
            food_list.append(line.strip())
    return food_list

def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove foods, 4 - Quit\n")
        if action == "1":
            new_food = input("Enter the name of food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == "2":
            print("Your favorite foods:")
            for food in foods:
                print(food)
        elif action == "3":
            idx = int(input("Which food to remove? "))
            foods.pop(idx - 1)
            write_foods(food)
        elif action == "4":
           break
main()
