from flask_wtf import FlaskForm
from wtforms.fields import (BooleanField, FieldList, PasswordField,
                            StringField, SubmitField, TextAreaField, TextField)
from wtforms.fields.html5 import DateField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

import utils
from main import API_URL


class RecoverForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    submit = SubmitField('Send new password')

    def validate_email(self, email):
        user = utils.get_url(API_URL+'/user/gsi/'+email.data)
        if user['id'] == None:
            raise ValidationError(
                'That email is invalid')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=3, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    id = StringField('Identification', validators=[
        DataRequired(), Length(3, 10)])
    name = StringField('Full Name', validators=[DataRequired(), Length(2, 30)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', [
        DataRequired(),
        EqualTo('confirm_password', message='Passwords must match'),
        Length(min=3, max=20)
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = utils.get_url(API_URL+'/user/gsi/'+email.data)
        if user['id']:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    ingredients = FieldList(TextField())
    submit = SubmitField('Save')


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Item')
