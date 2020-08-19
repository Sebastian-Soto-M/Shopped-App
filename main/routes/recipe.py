import json

import requests
from flask import Blueprint, redirect, render_template, request, url_for

from ..forms import RecipeForm


r_recipe = Blueprint('r_recipe', __name__,
                     static_folder='static')


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

@ r_recipe.route('/discover_recipes')
def discover_recipes():
    response = requests.get(
            'http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/recipe')
    data=json.loads(response.text)

    return render_template('views/base/discover_recipes.html', title='Recipes', data=data)
