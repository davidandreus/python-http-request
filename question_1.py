import requests

counter = 0


def check_name(pokemons):
    global counter
    for pokemon in pokemons:
        if pokemon["name"].count("at") > 0 and pokemon["name"].count("a") == 2:
            counter += 1


def question_1():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")
    if response.status_code == 200:
        while response.json()["next"] is not None:
            check_name(response.json()["results"])
            response = requests.get(response.json()["next"])
        return counter
    else:
        return False


print(question_1())
