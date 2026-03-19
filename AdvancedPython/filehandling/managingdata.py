#!/usr/bin/env python3

import re

# Writing, Reading, and Removing TV Shows
# function to write tv shows in a file
def write_show(shows):
    with open("show_list.txt", "w") as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

# Function to add a show to our shows list in dictionary format, and 
#write it to our file with the write_show function
def add_show(shows):
    title = input("What is the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("What is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)

# Function to read TV shows from a file
def read_shows():
    show_list = []
    with open("show_list.txt", "r") as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            show_list.append({'Title': data.group(1), 'Platform': data.group(2),
'Genre': data.group(3)})
    return show_list

# Function to print the list of shows for the user in a formatted way
def view(shows):
    print("Shows Lists")
    print("-----------------------")
    for idx, show in enumerate(shows):
        vowels = ["a", "e", "i", "o", "u"]
        a_or_an = "an" if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.{show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

