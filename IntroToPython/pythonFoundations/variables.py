#!/usr/bin/env python3

# x and y are variables and the number and string attached to it are values
x = 31
y = "Millicent"

print(x)
print(y)

# Casting variables
a = str("Hello, World!")
b = int(12)
c = float(3)

print(a)
print(b)
print(c)

# You can write different statements in one line by separating them with ;
print("I"); print("Love"); print("You")

# Print without a new line
print("I will visit in the evening.", end= " ")
print("Please prepare some pilau.")

# Print numbers
print(3); print(3 * 3); print(6 / 3)

# Print mix text and number
print("My favorite number is", 3)

# Reassigning value
m = 3
m = "me"
print(m) # it prints me because python already reassigned 3 to value me

# Get the type of value assigned to a variable
i = 3
j = "Jane"
print(type(i)); print(type(j))

# Case sensistive
c = 3
C = "mum"
print(c); print(C) # C will not overwrite c
