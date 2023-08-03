import requests
token = '8ddc500e9a9b49764fef25e8b39f7053'

response_add_pokemons = requests.post('https://api.pokemonbattle.me:9104/pokemons', json= {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},
headers={'trainer_token': token, 'content-type': 'application/json' })

print(response_add_pokemons.text)

response_put_pokemons = requests.put('https://api.pokemonbattle.me:9104/pokemons', json=
   {
    "pokemon_id": "5824",
    "name": "Ромашка",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
,
headers={'trainer_token': token, 'content-type': 'application/json' })

print(response_put_pokemons.text)

response_put_pokemons = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json=
   {
    "pokemon_id": "5824"
}
,
headers={'trainer_token': token, 'content-type': 'application/json' })

print(response_put_pokemons.text)

