import requests

# base url for the PokeAPI, must end with a slash since we append the name directly after it
base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(name):
    # build the full url for this specific pokemon
    # NOTE: no extra slash here since base_url already ends with one
    url = f"{base_url}{name}"

    # sends an HTTP GET request to the url and waits for a response
    response = requests.get(url)

    # status_code 200 means the request succeeded
    if response.status_code == 200:
        # .json() converts the raw response into a python dictionary
        data = response.json()
        return data
    else:
        # any other status code means something went wrong
        # common ones: 404 = not found, 500 = server error
        print(f"Error: {response.status_code}")
        return None  # explicit None so the caller knows the request failed


pokemon_name = input("Enter a pokemon name: ") #example: pikachu
info = get_pokemon_info(pokemon_name)

# only try to print details if info is not None (request actually succeeded)
if info:
    print(f"Name: {info['name']}")
    print(f"ID: {info['id']}")
    print(f"Height: {info['height']}")
    print(f"Weight: {info['weight']}")

