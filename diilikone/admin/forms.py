from flask_wtf import Form
from wtforms import validators
from wtforms.fields import PasswordField, StringField


class LoginForm(Form):
    email = StringField('Email', validators=[validators.input_required()])
    password = PasswordField('Password', validators=[validators.input_required()])
