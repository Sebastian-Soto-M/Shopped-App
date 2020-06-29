import os
from flask import Flask
from .base import r_base
from .cart import r_cart


def register_blueprints(app: Flask):
    app.register_blueprint(r_base)
    app.register_blueprint(r_cart)
