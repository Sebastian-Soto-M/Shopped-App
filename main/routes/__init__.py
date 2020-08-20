from main import app

from .base import r_base
from .cart import r_cart
from .recipe import r_recipe

app.register_blueprint(r_base)
app.register_blueprint(r_cart)
app.register_blueprint(r_recipe)
