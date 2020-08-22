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

    if recipes:
        for recipe in recipes:
            number=randrange(10)
            recipe['img_link']= "http://lorempixel.com/400/200/food/"+str(number)
            formatted_items=['-- Ingredients --']
            for key in recipe['items']:
                formatted_items.append("- "+key+", "+recipe['items'][key])
            recipe['items']=formatted_items
            formatted_steps=['-- Instructions --']
            for key in recipe['steps']:
                formatted_steps.append("- "+recipe['steps'][key])
            recipe['steps']=formatted_steps
            author_response = requests.get(
                                    API_URL+'/user/'+recipe['author'])

            recipe['author']=author_response.json()['name']

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
                formatted_items=['-- Ingredients --']
                for key in recipe['items']:
                    formatted_items.append("- "+key+", "+recipe['items'][key])
                recipe['items']=formatted_items
                formatted_steps=['-- Instructions -- ']
                for key in recipe['steps']:
                    formatted_steps.append("- "+recipe['steps'][key])
                recipe['steps']=formatted_steps
                recipe['author']=current_user.name


    return render_template('views/base/account/account_recipes.html', data=recipes, title='Cart', bg_img='side.jpg')
