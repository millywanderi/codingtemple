#!/usr/bin/env python3

# Open the file "demofile.txt" and append content to the file
with open("demofile.txt", "a") as f:
    f.write("Now the file has new content")

with open("demofile.txt") as f:
    print(f.read())

# Open the file "demofile.txt" and overwrite the content
with open("demofile.txt", "w") as f:
    f.write("Oops! I have deleted the content")

with open("demofile.txt") as f:
    print(f.read())
