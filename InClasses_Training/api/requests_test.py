import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

print(type(r.json()))
print(dir(requests))