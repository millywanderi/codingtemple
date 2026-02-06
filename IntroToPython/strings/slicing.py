#!/usr/bin/env python3

# Used to range characters

# Get characters from 2 to 5
name = "Kylie Kinsley"
print(name[2:5]) # output lie

# slice from start
name = "Kylie Kinsley"
print(name[:5]) # output Kylie

# slice from end
name = "Kylie Kinsley"
print(name[2:]) # lie Kinsley

# Negative slicing
name = "Kylie Kinsley"
print(name[-5:-2]) # nsl

# Slice int arrays
pos = [1, 2, 3, 4, 5]
print(pos[2:4]) # output 3, 4
