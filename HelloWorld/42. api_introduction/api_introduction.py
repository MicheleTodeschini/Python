import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    res = requests.get(url)


    if res.status_code == 200:
        pokemon_data = res.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {res.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")