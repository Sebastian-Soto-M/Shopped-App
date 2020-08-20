import json

import requests


def get_url(url: str) -> dict:
    response = requests.get(url)
    return json.loads(response.text)


def post(url: str, data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.post(url, json=data, headers=headers)
