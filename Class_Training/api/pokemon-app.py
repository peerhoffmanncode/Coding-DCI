import requests

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'

def fetch_pokemons(url):
    response = requests.get(url)
    data = response.json()
    file = open('pokemon.txt', 'a')
    for result in data['results']:    
        file.write(f"{result['name']}\n")
    file.close()

    if data['next']: # key error 
        fetch_pokemons(data['next'])

# call the function
fetch_pokemons(BASE_URL)        