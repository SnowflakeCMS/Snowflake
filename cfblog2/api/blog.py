# -*- encoding: utf-8 -*-
from cfblog2.api import APIBase, APICallException
from cfblog2.core.models import Blog as BlogModel
from cfblog2.core.utils import model_obj_to_dict
from . import api


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

    """ """
    def get(self, params, *args, **kwargs):
        result = []
        blog_rows = BlogModel.query.all()
        for b in blog_rows:
            result.append(model_obj_to_dict(b))
        return result


api.add_resource("/blog", Blog)