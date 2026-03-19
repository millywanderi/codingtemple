#!/usr/bin/env python3

import os

# Remove the file "call.txt"
os.remove("call.txt")

# Check if file exists, then delete it
if os.path.exists("call.txt"):
    os.remove("call.txt")
else:
    print("The file does not exist")

# Remove the folder "call"
os.rmdir("call")
