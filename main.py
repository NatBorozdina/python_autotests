'''
Test api
'''
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {"Content-Type": "application/json",
          "trainer_token": "fc5fcec17a1ff31db059bc66f344a975"
          }

body = {
   "name": "Акелло",
   "photo": "https://dolnikov.ru/pokemons/albums/034.png"
   }

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=10)
print(f'Статус код:{response.status_code}. Сообщение: {response.text}')


body = {
    "pokemon_id": 28406,
    "name": "Покемон",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=10)
print(f'Статус код:{response.status_code}. Сообщение: {response.text}')


response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=10)
print(f'Статус код:{response.status_code}. Сообщение: {response.text}')

