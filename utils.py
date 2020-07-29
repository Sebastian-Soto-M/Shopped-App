import json

import requests


def get_url(url: str) -> dict:
    response = requests.get(url)
    return json.loads(response.text)
