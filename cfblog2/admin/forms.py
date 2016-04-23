# -*- encoding: utf-8 -*-

from wtforms import Form, StringField, validators, PasswordField


class LoginForm(Form):
    username = StringField("Username", [validators.DataRequired(), validators.length(1, 100)])
    password = PasswordField("Login password", [validators.DataRequired()])
