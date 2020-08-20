import json
import string
import secrets

from main import bcrypt

import requests


def get_url(url: str) -> dict:
    response = requests.get(url)
    return json.loads(response.text)


def put(url: str, data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.put(url, json=data, headers=headers)


def post(url: str, data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.post(url, json=data, headers=headers)


def new_password() -> str:
    alphabet = string.ascii_letters + string.digits
    passwd = "".join(secrets.choice(alphabet) for i in range(8))
    return (passwd, bcrypt.generate_password_hash(passwd).decode('utf-8'))
