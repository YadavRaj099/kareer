import json
import random

def load_trends():

    with open("data/trends.json", "r") as file:
        trends = json.load(file)

    return trends


def get_random_trend():

    trends = load_trends()

    return random.choice(trends)