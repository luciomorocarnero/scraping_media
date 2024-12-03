import os
import json
from typing import Union
from pprint import pprint


def read(filename: str) -> dict:
    try:
        with open(filename, "r") as f:
            file = json.load(f)
    except Exception as e:
        raise ValueError(f"Could not read file.json: {e}")

    return file


def updateValue(d, path, value):
    keys = path.split(":")
    for key in keys[:-1]:
        if key not in d:
            d[key] = {}
        d = d[key]
    d[keys[-1]] = value


def findKey(
    data: Union[dict, list], key: str, path: str | None = None
) -> Union[str, None]:
    if not path:
        path = ""

    if isinstance(data, dict):
        if key in data:
            return path + ":" + key if path else key
        for k, v in data.items():
            result = findKey(v, key, path=f"{path}:{k}" if path else k)
            if result:
                return result

    elif isinstance(data, list):
        for index, item in enumerate(data):
            result = findKey(
                item, key, path=f"{path}[{index}]" if path else f"[{index}]"
            )
            if result:
                return result

        return None


class JsonHandler:
    def __init__(self, filename: str) -> None:
        if not os.path.isfile(filename):
            raise ValueError("File not finded")
        self.filename = filename


if __name__ == "__main__":
    a = {
        "hola": "asdas",
        "jiji": "asdas",
        "asdasdasdfb": "asdas",
        "joojo": {
            "iaaa": "asdahf",
            "ooo": {
                "hasdasd": ["jiji", {"chau": "hola"}],
            },
        },
    }
    pprint(a)
