import json

import requests
from flask import Blueprint, redirect, render_template, request, url_for

from ..forms import RecipeForm


r_recipe = Blueprint('r_recipe', __name__,
                     static_folder='static')


@r_recipe.route('/recipe', methods=['GET', 'POST'])
def recipe():
    form = RecipeForm()
    response = requests.get(
        'http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/recipe')
    print(json.loads(response.text))

    if form.validate_on_submit():
        instructions = form.instructions.data.splitlines()
        items = form.ingredients.data
        #import pdb; pdb.set_trace()
        print (form.ingredients.data)
        item_count=1
        items_list=[]
        item_string=""
        for item in items:
            if item_count % 2 == 0 and item_count>0:
                item_string=item_string+","+item
                items_list.append(item_string)
                item_string=""
                print('quantity')
            else:
                item_string=item
                print('item')
            item_count=item_count+1
        dict(item.split(",") for item in items_list)

        res_dct = {items[i]: items[i + 1] for i in range(0, len(items), 2)}
        print (res_dct)
        print(items_list)
        instructions_json = dict(enumerate(instructions))
        items_json = dict(enumerate(items_list))
        data = {
            "status": "ACTIVE",
            "author": "01236446",
            f"items": res_dct,
            "data":
                {f"name": form.name.data,
                 f"description": form.description.data,
                 f'steps': instructions_json}

        }
        print(data)
        r = requests.post(
            'http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/recipe', json=data)

        print(r.status_code)
        return redirect(url_for('.recipe'))

    return render_template('views/base/recipe.html', title='Recipes', form=form, img='recipe.jpg')
