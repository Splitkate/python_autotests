import requests



URL =  'https://api.pokemonbattle.ru/v2'
TOKEN = '98f59cad947d78ffd6ce47b1bff68676'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

change = {
    "pokemon_id": "118043",
    "name": "korn",
    "photo_id": 2
}


body_create = {
    "name": "Kissa",
    "photo_id": 2
}


body_pokeball = {
    "pokemon_id": "118042"
}


'''response = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''

'''response = requests.put(url=f'{URL}/pokemons',  headers = HEADER, json = change)
print(response.text)'''

response = requests.post(url=f'{URL}/trainers/add_pokeball',  headers = HEADER, json = body_pokeball)
print(response.text)