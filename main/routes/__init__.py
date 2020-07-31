from main import app

from .base import r_base
from .cart import r_cart
from .recipe import r_recipe

app.register_blueprint(r_base)
app.register_blueprint(r_cart)
app.register_blueprint(r_recipe)


@app.errorhandler(404)
def page_not_found(e):
    if current_user.is_authenticated:
        return render_template('views/404_dashboard.html',
                               title='Not Found'), 404
    else:
        return render_template('views/404_basic.html', title='Not Found'), 404
