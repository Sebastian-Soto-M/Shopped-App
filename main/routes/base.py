import json

import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

import utils
from main import API_URL, bcrypt

from ..forms import LoginForm
from ..models import User

r_base = Blueprint('r_base', __name__, static_folder='static')


@r_base.route('/login', methods=['GET', 'POST'])
def login():
    print('before user validation')
    if current_user.is_authenticated:
        return redirect(url_for('.home'))
    form = LoginForm()
    if form.validate_on_submit():
        data = utils.get_url(API_URL+'/user/gsi/'+form.email.data)
        if data["id"] != None:
            user = User.to_object(utils.get_url(API_URL+'/user/'+data['id']))
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else \
                    redirect(url_for('index'))
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
    logout_user()
    return redirect(url_for('.home'))


@ r_base.route('/account')
def account():
    return render_template('views/base/index.html', title='Account')


@ r_base.route('/')
def home():
    return render_template('views/base/index.html', title='Home')
