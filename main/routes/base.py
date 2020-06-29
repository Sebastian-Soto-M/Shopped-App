from flask import Blueprint, redirect, render_template, url_for, request

r_base = Blueprint('r_base', __name__, static_folder='static')


@r_base.route('/signin')
def signin():
    return render_template('views/base/signin.html')


@r_base.route('/signup')
def signup():
    return render_template('views/base/index.html')


@r_base.route('/signout')
def signout():
    return render_template('views/base/index.html')


@r_base.route('/account')
def account():
    return render_template('views/base/index.html')


@r_base.route('/')
def home():
    return render_template('views/base/index.html')
