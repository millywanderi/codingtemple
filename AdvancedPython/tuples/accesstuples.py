#!/usr/bin/env python3

# Print the second item in the tuple
mytuple = ("Steve", "Millie", "Kylie", "Lyle")
print(mytuple[1])

# Print the last item of the tuple
mytuple = ("Steve", "Millie", "Kylie", "Lyle")
print(mytuple[-1])

# Return the third, fourth, and fifth item
mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(mytuple[2:5])

# Range of Negative Indexes
mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(mytuple[-4:-1])

# Check if "apple" is present in the tuple
mytuple = ("apple", "banana", "mango")
if "apple" in mytuple:
    print("Yes, 'apple' is in the fruit tuple")
