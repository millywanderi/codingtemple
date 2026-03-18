#!/usr/bin/env python3

# open and read a file
f = open("demofile.txt")
print(f.read())

# Using the with keyword
with open("demofile.txt") as f:
    print(f.read())

# Close the file when you are finished with it
f = open("demofile.txt")
print(f.readline())
f.close()
