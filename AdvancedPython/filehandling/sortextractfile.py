#!/usr/bin/env python3

# sorting lists
flowers = ["Wysteria", "Sunflowers", "Orchids", "Marigolds"]

with open("garden.txt", "w") as file:
    for flower in flowers:
        file.write(flower + "\n")

# Extract list
flowers = []

with open("garden.txt", "r") as file:
    for line in file:
        flowers.append(line.strip())
print(flowers)
