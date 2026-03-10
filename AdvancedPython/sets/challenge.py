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


"""
Exercise 5: Working with Set Operations
Create two sets of your favorite vacation destinations.
Use union to find all the unique destinations.
Use intersection to find common destinations.
Use difference to find destinations unique to one of your sets.
"""
set1 = {"Dubai", "Diani", "Malysia", "Georgia"}
set2 = {"Georgia", "Maasai Mara", "Capetown"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


"""
Final Challenge: Email List Deduplication
You have two email lists, but some people may be in both. Write a function to:

Remove duplicates.
Show which emails exist in both lists.
Show emails that are unique to each list.
"""
def clean_email_list(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    # Remove duplicates
    all_unique = set1.union(set2)
    print("All unique emails:", all_unique)

    # common emails
    common_emails = set1.intersection(set2)
    print("All common emails:", common_emails)

    # email each unique list
    unique_emails = set1.symmetric_difference(set2)
    print("Emails unique to each list:", unique_emails)

email_list1 = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "a@gmail.com"]
email_list2 = ["a@gmail.com", "d@gmail.com", "e@gmail.com"]

clean_email_list(email_list1, email_list2)
