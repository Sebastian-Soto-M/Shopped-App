from flask import Blueprint, redirect, render_template, url_for, request
from ..forms import RecipeForm

r_recipe = Blueprint('r_recipe', __name__,
                   static_folder='static')

@r_recipe.route('/recipe', methods=['GET', 'POST'])
def recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        print('saving recipe')
        return redirect(url_for('.recipes'))
   
    return render_template('views/base/recipe.html', title='Recipes', form=form,img='recipe.jpg')