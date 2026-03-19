#!/usr/bin/env python3

# sorting lists
flowers = ["Wysteria", "Sunflowers", "Orchids", "Marigolds"]

with open("garden.txt", "w") as file:
    for flower in flowers:
        file.write(flower + "\n")
