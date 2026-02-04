#!/usr/bin/env python3

# x and y are variables and the number and string attached to it are values
x = 31
y = "Millicent"
print(x)
print(y)

# many values to multiple variables
e, f, g = "Monday", "Tuesday", "Wednesday"
print(e); print(f); print(g)

# One value to multiple variables
o = p = q = "Purple"
print(o); print(p); print(q)

# Unpack a collection
colors = ["beige", "blue", "white", "yellow"]
w, x, y, z = colors
print(w); print(x); print(y); print(z)

# Casting variables
a = str("Hello, World!")
b = int(12)
c = float(3)

print(a)
print(b)
print(c)

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

# Global variables. They are written outside the function
x = "Millicent"

def myfunc():
    x = "Wanderi"
    print("My name is " + x)
myfunc()
print("My name is " + x)

# Use of global keyword to create a variable inside a function
x = "blue"

def myfunc():
    global x
    x = "beige"

myfunc()
print("My favorite color is " + x)
