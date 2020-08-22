import json
import os

import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

import utils
from main import API_URL, bcrypt
from random import randrange


from ..forms import LoginForm, RecoverForm, RegisterForm
from ..models import User

r_account = Blueprint('r_account', __name__, static_folder='static')


@r_account.route('/account/info')
def info():
    recipes=[]
    response = requests.get(
                             API_URL+'/recipe/')
    recipes=response.json()
    for recipe in recipes:
        if recipe['id'] not in current_user.shopping_lists:
            recipes.remove(recipe)
        #import pdb; pdb.set_trace()
        #response = requests.get(API_URL+'/recipe/'+recipe+"/"+current_user.id)
        #recipe= response.json()
        #recipes.append(recipe)


    if recipes:
        for recipe in recipes:
            number=randrange(10)
            recipe['img_link']= "http://lorempixel.com/400/200/food/"+str(number)

    return render_template('views/base/account/account_info.html', data=recipes, title='Cart', bg_img='side.jpg')


@r_account.route('/account/cart')
def cart():
    return render_template('views/base/account/account_cart.html', title='Cart', bg_img='side.jpg')


@r_account.route('/account/recipes')
def recipes():
    response = requests.get(
             API_URL+'/recipe/'+current_user.id)
    recipes=response.json()
    if recipes:

            for recipe in recipes:
                number=randrange(10)
                recipe['img_link']= "http://lorempixel.com/400/200/food/"+str(number)

    return render_template('views/base/account/account_recipes.html', data=recipes, title='Cart', bg_img='side.jpg')
