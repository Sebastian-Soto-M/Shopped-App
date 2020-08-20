import json
import os

import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

import utils
from main import API_URL

from ..forms import LoginForm
from ..models import User

r_base = Blueprint('r_base', __name__, static_folder='static')


@r_base.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.home'))
    form = LoginForm()
    if form.validate_on_submit():
        data = utils.get_url(API_URL+'/user/gsi/'+form.email.data)
        if data["id"] != None:
            user = User.to_object(utils.get_url(API_URL+'/user/'+data['id']))
            login_user(user)
            next = flask.request.args.get('next')
            return redirect(next or url_for('.home'))
        else:
            flash(f'Login unsuccessful. Please check your email and password.',
                  'danger')
    return render_template('views/base/login.html', title='Log In', form=form,
                           img='bgimg.jpg')


@ r_base.route('/register')
def register():
    return render_template('views/base/register.html', title='Register')


@ r_base.route('/logout')
def logout():
    return render_template('views/base/index.html', title='Logout')


@ r_base.route('/account')
def account():
    return render_template('views/base/index.html', title='Account')


@ r_base.route('/')
def home():
    print(os.environ['TEAM'])
    return render_template('views/base/index.html', title='Home')
