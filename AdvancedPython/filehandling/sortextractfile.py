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

# Storing and Extracting Dictionaries
clubs = {
    "Driver": "Cobra",
    "Irons": "Sirixion",
    "Hybrid": "Callway",
    "Putter": "Ping"
}

with open("golf_bag.txt", "w") as file:
    for club, brand in clubs.items():
        file.write(f"{club}: {brand}\n")

# extract dictionary data
golf_clubs = {}

with open("golf_bag.txt", "r") as file:
    for line in file:
        club, brand = line.strip().split(": ")
        golf_clubs[club] = brand
print(golf_clubs)
