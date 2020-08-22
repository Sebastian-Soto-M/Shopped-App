from abc import ABC, abstractmethod

from flask_login import LoginManager, UserMixin

import utils
from main import API_URL, login_manager


@login_manager.user_loader
def load_user(user_id):
    usr_data = utils.get_url(API_URL+'/user/'+user_id)
    return User.to_object(usr_data)


class ResponseObject(ABC):
    @staticmethod
    @abstractmethod
    def to_object(cls, obj: dict):
        return self


class User(UserMixin, ResponseObject):
    def __init__(self, id, name="", email="", password="",
                 status="", shopping_lists=[]):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.shopping_lists = shopping_lists

    def to_object(obj: dict):
        return User(
            id=obj['id'],
            name=obj['name'],
            email=obj['email'],
            password=obj['password'],
            status=obj['status'],
            shopping_lists=obj['shopping_lists'],
        )

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "status": self.status,
            "shopping_lists": self.shopping_lists,
        }


class Cart(ResponseObject):
    def __init__(self, author: str, items: dict):
        self.author = author
        self.items = items

    def to_object(obj: dict):
        return Cart(
            author=obj['author'],
            items=obj['items'],
        )

    def to_json(self):
        return {
            "author": self.author,
            "items": self.items
        }
