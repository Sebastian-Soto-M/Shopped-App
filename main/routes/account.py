import json
import os

import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

import utils
from main import API_URL, bcrypt

from ..forms import LoginForm, RecoverForm, RegisterForm
from ..models import User

r_account = Blueprint('r_account', __name__, static_folder='static')


@r_account.route('/account/info')
def info():
    return render_template('views/base/account/account_info.html', title='Account', bg_img='side.jpg')


@r_account.route('/account/cart')
def cart():
    return render_template('views/base/account/account_cart.html', title='Cart', bg_img='side.jpg')


@r_account.route('/account/recipes')
def recipes():
    return render_template('views/base/account/account_recipes.html', title='Cart', bg_img='side.jpg')
