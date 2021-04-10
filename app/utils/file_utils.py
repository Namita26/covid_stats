import json


def read_json(filename: str) -> object:
    with open(filename, encoding="utf-8") as f:
        return json.load(f)