# -*- encoding:utf-8 -*-

from cfblog2.restful.flask import FlaskResource
from cfblog2.restful.params import Text, Password
from . import api


class Auth(FlaskResource):
    name = "auth"
    username = Text()
    password = Password()

    def __init__(self):
        super(Auth, self).__init__()

    """Auth API"""
    def post(self, params):
        return "auth"

api.add_resource("/auth", Auth)
