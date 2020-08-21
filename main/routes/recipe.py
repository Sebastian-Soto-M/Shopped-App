import json
from random import randrange

import requests
from flask import Blueprint, redirect, render_template, request, url_for

from ..forms import RecipeForm

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
            "author": "01236446",
            f"items": items_json,
            f'steps': instructions_json,
            "data":
                {f"name": form.name.data,
                 f"description": form.description.data}

        }
        print(data)
        r = requests.post(
            'http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/recipe', json=data)

        print(r.status_code)
        return redirect(url_for('.recipe'))

    return render_template('views/base/recipe.html', title='Recipes', form=form, img='recipe.jpg')

@ r_recipe.route('/discover_recipes', methods=['GET', 'POST'])
def discover_recipes():
    form=RecipeForm()
    response = requests.get(
            'http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/recipe')
    recipes=response.json()

    if form.is_submitted():
        search_recipe_results=[]
        for item in response.json():
            #import pdb; pdb.set_trace()
            if form.name.data:
                print(form.name.data)
                print(item['data']['name'])
                if (form.name.data).lower()  not in (item['data']['name']).lower():
                    recipes.remove(item)

    if recipes:

        for recipe in recipes:
            author_id=recipe['author']
            print(author_id)
            author_response = requests.get(
                        f'http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/user/{author_id}')
            number=randrange(10)
            recipe['img_link']= "http://lorempixel.com/400/200/food/"+str(number)
            recipe['author']=author_response.json()['name']

    return render_template('views/base/discover_recipes.html', title='Recipes', data=recipes, img='discover.jpeg', form=form)


@ r_recipe.route('/add_recipe', methods=[ 'POST', 'GET'])
def add_recipe():
    form= RecipeForm()
    print(request.args.get('id'))
    return render_template('views/base/recipe.html', title='Recipes', form=form, img='recipe.jpg')
