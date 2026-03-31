#!/usr/bin/env python3

import json
import requests

# Make a GET request to the PokeAPI for Pikachu
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: response.status_code")
