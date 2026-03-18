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

# Return the 5 first characters of the file
f = open("demofile.txt")
print(f.read(5))

# Loop through the file line by line
with open("demofile.txt") as f:
    for x in f:
        print(x)
