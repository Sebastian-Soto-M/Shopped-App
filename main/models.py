from abc import ABC, abstractmethod


class ResponseObject(ABC):
    @staticmethod
    @abstractmethod
    def to_object(cls, obj: dict):
        return self


class User(ResponseObject):
    def __init__(self, id, name="", email="", password="", birth_date=None,
                 status=None, shopping_lists=[], rating=0, rating_amount=0,
                 rating_sum=0):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.status = status
        self.shopping_lists = shopping_lists
        self.rating = rating
        self.rating_amount = rating_amount
        self.rating_sum = rating_sum

    def to_object(obj: dict):
        return User(
            id=obj['id'],
            name=obj['name'],
            password=obj['password'],
            birth_date=obj['birthDate'],
            status=obj['status'],
            shopping_lists=obj['shoppingLists'],
            rating=obj['rating'],
            rating_amount=obj['ratingAmount'],
            rating_sum=obj['ratingSum']
        )
