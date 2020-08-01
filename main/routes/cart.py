from flask import Blueprint, redirect, render_template, request, url_for

r_cart = Blueprint('r_cart', __name__, url_prefix='/cart',
                   static_folder='static')


@r_cart.route('/cart/home')
def home():
    return redirect(url_for('base_r.home'))


@r_cart.route('/update')
def signin():
    return render_template('views/cart/index.html')


@r_cart.route('/history')
def signup():
    return render_template('views/cart/index.html')
