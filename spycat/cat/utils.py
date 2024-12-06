import requests

BREEDS_URL = "https://api.thecatapi.com/v1/breeds"


def validate_breed(breed_name):
    response = requests.get(BREEDS_URL)

    if response.status_code != 200:
        raise Exception("Failed to fetch data from TheCatAPI. Please try again later.")

    breeds = response.json()
    breed_names = [breed['name'] for breed in breeds]

    if breed_name not in breed_names:
        raise ValueError(f"The breed '{breed_name}' is not valid.")

    return True