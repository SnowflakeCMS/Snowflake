# -*- encoding: utf-8 -*-
from cfblog2.api import APIBase, APICallException


class BlogException(APICallException):
    pass


class Blog(APIBase):
    restful_method = {"post", "get"}
    name = "Blog"
    desc = "Blog resource api"
    need_auth = True

    def __init__(self, *args, **kwargs):
        super(Blog, self).__init__(*args, **kwargs)

    """Post blog api"""
    def post(self, params, *args, **kwargs):
        pass

    def get(self, params, *args, **kwargs):
        pass

