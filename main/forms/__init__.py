from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, Email, Length, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Decription', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    items = TextAreaField('Items', validators=[DataRequired()])
    flist = FieldList(TextField())
    submit = SubmitField('Save')

class Sample(FlaskForm):
    name = StringField()
    description = StringField('Decription', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    items = TextAreaField('Items', validators=[DataRequired()])
    ingredients = FieldList(TextField())
    submit = SubmitField('Submit')
