from flask import Blueprint, redirect, render_template, request, url_for
from ..forms import LoginForm

r_base = Blueprint('r_base', __name__, static_folder='static')


@r_base.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('logged in')
        return redirect(url_for('.home'))
    return render_template('views/base/login.html', title='Log In', form=form,
                           img='bgimg.jpg')


@r_base.route('/register')
def register():
    return render_template('views/base/register.html', title='Register')


@r_base.route('/logout')
def logout():
    return render_template('views/base/index.html', title='Logout')


@r_base.route('/account')
def account():
    return render_template('views/base/index.html', title='Account')


@r_base.route('/')
def home():
    return render_template('views/base/index.html', title='Home')
