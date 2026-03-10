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
favorite_movies = {"Prison Break", "Broke Girls", "In the Middle",
                   "Beauty in Black", "Fatal Seduction"}
for movie in favorite_movies:
    print(movie)


"""
Exercise 3: Set Modification Practice
Create a set of at least 4 of your favorite foods.
Add one more food item to the set.
Write code to check if a specific food item is in the set, then print the result.
"""
favorite_foods = {"pilau", "nyama choma", "mukimo", "chapati"}
favorite_foods.add("ugali")
print("ugali" in favorite_foods)
print(favorite_foods)


"""
Exercise 4: Comparing Sets
Create two sets of your favorite sports or hobbies.
Check if one set is a subset of the other.
Check if one set is a superset of the other.
"""
sports1 = {"handball", "valleyball"}
sports2 = {"handball", "valleyball", "netball", "table tennis"}

print(sports1.issubset(sports2))
print(sports2.issuperset(sports1))
