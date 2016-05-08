# -*- encoding:utf-8 -*-
from cfblog2.core.models import User
from cfblog2.restful.flask import FlaskResource
from cfblog2.restful.types import String, Password
from . import api


class Auth(FlaskResource):
    restful_method = {"post"}
    name = "auth"
    username = String()
    password = Password()

    def __init__(self):
        super(Auth, self).__init__()

    """Auth API"""
    def post(self, params, *args, **kwargs):
        p_username = params["username"]
        p_password = params["password"]

        user = User.query.filter_by(username=p_username, password=p_password).first()
        # user = User.query.all()[0]
        if user is None:
            return {"code": 1, "msg": "Not auth", "extra": None}
        else:
            return {"code": 2, "msg": "Success", "extra": "This should be token" + repr(user.username)}


api.add_resource("/auth", Auth)
