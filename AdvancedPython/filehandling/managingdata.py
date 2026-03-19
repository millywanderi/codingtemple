#!/usr/bin/env python3

import re

# Writing, Reading, and Removing TV Shows
# function to write tv shows in a file
def write_show(shows):
    with open("show_list.txt", "w") as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")
