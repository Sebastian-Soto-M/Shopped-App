from main import app

from .base import r_base
from .bundle import r_bundle
from .cart import r_cart
from .recipe import r_recipe

app.register_blueprint(r_base)
app.register_blueprint(r_bundle)
app.register_blueprint(r_cart)
app.register_blueprint(r_recipe)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/base/404.html', title='Not Found'), 404
