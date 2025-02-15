import json
from random import randrange

import requests
from flask import Blueprint, redirect, render_template, request, url_for

from ..forms import RecipeForm
from flask_login import current_user

import utils
from main import API_URL


r_recipe = Blueprint('r_recipe', __name__,
                     static_folder='static')


@r_recipe.route('/recipe/home')
def home():
    return redirect(url_for('base_r.home'))


@r_recipe.route('/recipe', methods=['GET', 'POST'])
def recipe():
    form = RecipeForm()

    if form.validate_on_submit():
        instructions = form.instructions.data.splitlines()
        items = form.ingredients.data
        items_json = {items[i]: items[i + 1] for i in range(0, len(items), 2)}

        instructions_json = dict(enumerate(instructions))
        data = {
            "status": "ACTIVE",
            "author": current_user.id,
            f"items": items_json,
            f'steps': instructions_json,
            "data":
                {f"name": form.name.data,
                 f"description": form.description.data}

        }
        print(data)
        r = requests.post(
            API_URL+'/recipe', json=data)

        print(r.status_code)
        return redirect(url_for('.recipe'))

    return render_template('views/base/recipe.html', title='Recipes', form=form, img='recipe.jpg')

@ r_recipe.route('/discover_recipes', methods=['GET', 'POST'])
def discover_recipes():
    form=RecipeForm()
    response = requests.get(
             API_URL+'/recipe')
    recipes=response.json()

    if form.is_submitted():
        search_recipe_results=[]
        for item in response.json():
            if form.name.data:
                print(form.name.data)
                print(item['data']['name'])
                if (form.name.data).lower()  not in (item['data']['name']).lower():
                    recipes.remove(item)

    if recipes:
        #import pdb; pdb.set_trace()

        for recipe in recipes:
            author_id=recipe['author']
            print(author_id)
            author_response = requests.get(
                        API_URL+'/user/'+author_id)
            number=randrange(10)
            recipe['img_link']= "http://lorempixel.com/400/200/food/"+str(number)
            recipe['author']=author_response.json()['name']

    return render_template('views/base/discover_recipes.html', title='Recipes', data=recipes, img='discover.jpeg', form=form)


@ r_recipe.route('/add_recipe', methods=[ 'POST', 'GET'])
def add_recipe():
    form= RecipeForm()
    recipe_id=request.args.get('id')

    if recipe_id not in current_user.shopping_lists:
        response = requests.get(API_URL+'/recipe/'+recipe_id+"/"+current_user.id)
        if response.text is not '':
            return redirect(url_for('r_account.recipes'))
        current_user.shopping_lists.append(recipe_id)
        data = {
                    "id": current_user.id,
                    "name": current_user.name,
                    "email": current_user.email,
                    'password': current_user.password,
                    'shopping_lists': current_user.shopping_lists,
                    'status': current_user.status
                }
        print(data)
        r = requests.put(
            API_URL+'/user', json=data)
    return redirect(url_for('r_account.info'))