from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from ..forms import ItemForm
from main import API_URL
from ..models import User
from ..models import Cart
import utils

r_cart = Blueprint(
    'r_cart', __name__, static_folder='static'
)


@login_required
@r_cart.route('/cart/active/', methods=['GET', 'POST'])
def get_active():
    form = ItemForm()
    cart = utils.get_url(API_URL+'/cart/active/'+current_user.id)['items']
    if cart == None:
        cart = []
    if form.validate_on_submit():
        items = {}
        items[form.name.data] = form.amount.data
        cart = Cart(author=current_user.id, items=items)
        utils.put(API_URL+'/cart', cart.to_json())
        return redirect(url_for('.get_active'))

    return render_template('views/base/account/account_cart.html', title='Cart', bg_img='side.jpg', form=form, cart=cart)


@login_required
@r_cart.route('/cart/new')
def replace():
    utils.post(API_URL+'/cart/replace/'+current_user.id, "")
    return redirect(url_for('.get_active'))
