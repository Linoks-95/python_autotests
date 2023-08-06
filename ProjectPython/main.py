import requests

host = 'https://api.pokemonbattle.me:9104'
token = 'e58aa25edcb20c27b4642e296789d011'

response_pokemon = requests.post(f'{host}/pokemons', json = {"name": "generate",
"photo": "generate"}
        , headers = {'Content-Type' : 'application/json',
                  'trainer_token': token})
print(response_pokemon.text)

response_put_pokemon = requests.put(f'{host}/pokemons', json = {"pokemon_id": "5933", "name": "Капитошка",
"photo": "https://dolnikov.ru/pokemons/albums/008.png"}
        , headers = {'Content-Type' : 'application/json',
                  'trainer_token': token})
print(response_put_pokemon.text)

response_add_pokeball_pokemon = requests.post(f'{host}/trainers/add_pokeball', json = {"pokemon_id": "5938"}
        , headers = {'Content-Type' : 'application/json',
                  'trainer_token': token})
print(response_add_pokeball_pokemon.text)