import os
from flask import Flask
from .base import r_base
from .cart import r_cart
from .recipe import r_recipe



def register_blueprints(app):
    app.register_blueprint(r_base)
    app.register_blueprint(r_cart)
    app.register_blueprint(r_recipe)

