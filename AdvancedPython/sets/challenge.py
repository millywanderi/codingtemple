#!/usr/bin/env python3

"""
# Exercise 1: Practice Creating Sets
Create a list of your favorite hobbies, making sure to repeat a few of them.
Convert the list into a set to automatically remove the duplicates.
Print both the original list and the set to compare.
"""
favoritehobbies = ["coding", "travelling", "reading", "coding", "watching"]
hobbies = set(favoritehobbies)
print(favoritehobbies)
print(hobbies)

"""
# Exercise 2: Loop Through a Set
Create a set of your top 5 favorite books or movies.
Write a for loop to print each item in the set.
"""
favorite_movies = {"prison break", "broke girls", "in the middle",
                   "beauty in black", "fatal seduction"}
for movie in favorite_movies:
    print(movie)
