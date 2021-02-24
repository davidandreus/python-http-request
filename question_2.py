import requests


def question_2():
    response = requests.get(
        "https://pokeapi.co/api/v2/pokemon-species/raichu/")
    if response.status_code == 200:
        pokemons = []
        for egg_group in response.json()["egg_groups"]:
            response_group = requests.get(egg_group["url"]).json()[
                "pokemon_species"]
            if len(pokemons) == 0:
                pokemons = response_group
            else:
                filtered_object = filter(
                    lambda pokemon: pokemon not in pokemons,
                    response_group
                )
                pokemons.extend(filtered_object)
        return len(pokemons)
    else:
        return False


print(question_2())
