import requests


def question_1():
    counter = 0
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")
    if response.status_code == 200:
        while response.json()["next"] is not None:
            for pokemon in response.json()["results"]:
                if pokemon["name"].count("at") > 0 and pokemon["name"].count("a") == 2:
                    counter += 1
            response = requests.get(response.json()["next"])
        return counter
    else:
        return False


print(question_1())
