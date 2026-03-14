import json
from pathlib import Path


def get_trends():
    path = Path("data/trends.json")

    if not path.exists():
        return [
            "AI careers are trending globally",
            "Data Science demand rising rapidly",
            "Cybersecurity jobs growing worldwide",
            "Cloud engineers highly demanded",
            "Product management attracting tech graduates"
        ]

    with open(path, "r") as f:
        trends = json.load(f)

    return trends