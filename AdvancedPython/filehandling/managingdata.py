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
