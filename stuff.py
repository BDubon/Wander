#!/usr/bin/env python3
# Import libraries
import requests

# MAke code more robust
ability = input('Enter ability: ')
ability = ability.lower()            # Lower case to normalize
ability = ability.split()            # Split to then join multiple letters
ability = '-'.join(ability)          # Join list

# URL to request data
url = 'https://pokeapi.co/api/v2/ability/' + ability

# Request data and convert to python dictionary
response = requests.request('GET', url)
data = response.json()               # Convert to json/dictionary

# Extract every pokemon with this ability
for i in data['pokemon']:
    name = i['pokemon']['name']
    print('Pokemon with this ability:', name)

# Extract ability's effect
effect = data['effect_entries'][0]['short_effect']
print('')
print('Effect:', effect)

