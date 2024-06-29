import json


def save(garage):
    with open("garage.json", "w") as file:
        json.dump(garage, file)


def load():
    with open("garage.json", "r") as file:
        garage = json.load(file)
        return garage
