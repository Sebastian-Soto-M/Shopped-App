from flask import Blueprint, redirect, render_template, url_for, request

r_base = Blueprint('r_base', __name__, static_folder='static')


@r_base.route('/login')
def login():
    return render_template('views/base/login.html', img='bgimg.jpg')


@r_base.route('/register')
def logup():
    return render_template('views/base/register.html')


@r_base.route('/logout')
def logout():
    return render_template('views/base/index.html')


@r_base.route('/account')
def account():
    return render_template('views/base/index.html')


@r_base.route('/')
def home():
    return render_template('views/base/index.html')
