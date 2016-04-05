# -*- encoding: utf-8 -*-

from wtforms import Form, StringField, validators, PasswordField


class LoginForm(Form):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Login password", [validators.DataRequired()])
