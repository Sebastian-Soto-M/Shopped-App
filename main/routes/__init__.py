from main import app

from .base import r_base
from .account import r_account
from .cart import r_cart
from .recipe import r_recipe

app.register_blueprint(r_base)
app.register_blueprint(r_account)
app.register_blueprint(r_cart)
app.register_blueprint(r_recipe)
