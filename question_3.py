import requests
import re


def question_3():
    max_weight = 0
    min_weight = 0
    response = requests.get("https://pokeapi.co/api/v2/type/")
    if response.status_code == 200:
        filtered_object = filter(
            lambda type: type["name"] == "fighting",
            response.json()["results"]
        )
        url = list(filtered_object)[0]["url"]
        response_type = requests.get(url).json()
        filtered_pokemons = filter(lambda pokemon: int(re.search(
            '/pokemon/(.*)/', pokemon["pokemon"]["url"]).group(1)) <= 151,
            response_type["pokemon"]
        )

        for pokemon in filtered_pokemons:
            request_weight = requests.get(
                pokemon["pokemon"]["url"]).json()["weight"]
            if min_weight == 0:
                min_weight = request_weight
            if request_weight > max_weight:
                max_weight = request_weight
            if request_weight < min_weight:
                min_weight = request_weight

        return [max_weight, min_weight]
    else:
        return False


print(question_3())
