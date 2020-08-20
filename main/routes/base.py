import pdb
import json
from datetime import datetime

import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

import utils
from main import API_URL, bcrypt

from ..forms import LoginForm, RegisterForm
from ..models import User

r_base = Blueprint('r_base', __name__, static_folder='static')


@r_base.route('/login', methods=['GET', 'POST'])
def login():
    import pdb
    if current_user.is_authenticated:
        return redirect(url_for('.home'))

    form = LoginForm()

    if form.validate_on_submit():
        usr_id = utils.get_url(API_URL+'/user/gsi/'+form.email.data)
        if usr_id != None:
            user = User.to_object(utils.get_url(API_URL+'/user/' + usr_id))
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else \
                    redirect(url_for('.home'))
        else:
            flash(f'Login unsuccessful. Please check your email and password.',
                  'danger')
    return render_template('views/base/login.html', title='Log In', form=form,
                           img='bgimg.jpg')


@r_base.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(
            id=form.id.data,
            name=form.name.data,
            email=form.email.data,
            password=hashed_pw
        )
        utils.post(API_URL+'/user/', user.to_json())
        return redirect(url_for('r_base.login'))

    return render_template('views/base/register.html',
                           title='Register', form=form, style_sheet=True,
                           bg_img='bgimg.jpg')


@r_base.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.home'))


@r_base.route('/account')
def account():
    return render_template('views/base/index.html', title='Account')


@r_base.route('/')
def home():
    return render_template('views/base/index.html', title='Home')


@r_base.errorhandler(404)
def page_not_found(e):
    return render_template('views/base/404.html', title='Not Found'), 404
