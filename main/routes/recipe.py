from flask import Blueprint, redirect, render_template, url_for, request
from ..forms import RecipeForm
import requests
import json


r_recipe = Blueprint('r_recipe', __name__,
                   static_folder='static')

@r_recipe.route('/recipe', methods=['GET', 'POST'])
def recipe():
    form = RecipeForm()
    response = requests.get('http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/recipe')
    print (json.loads(response.text))

    
    if form.validate_on_submit():
        instructions=form.instructions.data.splitlines()
        items=form.items.data.splitlines()
        print(instructions)
        print(items)
        instructions_json=dict(enumerate(instructions))
       
        print(instructions_json)
        data = {
            "status": "ACTIVE",
            "author": "01236446",
            "items":
                {"chinken":"1",
                "garlic":"2"},
            "data":  
                {f"name": form.name.data,
                f"description": form.description.data,
                f'steps' : instructions_json }
                
        }
        print(data)
        r = requests.post('http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1/recipe', json=data)
       
        # print(r.status_code)
        return redirect(url_for('.recipe'))
   
    return render_template('views/base/recipe.html', title='Recipes', form=form,img='recipe.jpg')