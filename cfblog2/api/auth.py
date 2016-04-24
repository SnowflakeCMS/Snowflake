# -*- encoding:utf-8 -*-
from flask import render_template, redirect, url_for

from cfblog2.restful import Resource
from . import api


class Auth(Resource):
    def __init__(self):
        pass

    """Auth API"""
    def post(self):
        return "auth"

api.add_url_rule("/auth", view_func=Auth.as_view("auth"))
