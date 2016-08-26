# -*- encoding: utf-8 -*-
from cfblog2 import db
from cfblog2.api import APIBase, APICallException
from cfblog2.core.models import Blog as BlogModel
from cfblog2.core.utils import model_obj_to_dict
from cfblog2.restful.resource import ResourceFilter
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
    @ResourceFilter(methods=["post"])
    def new_blog(self, params, blog_id):
        assert blog_id is None
        # TODO use param validator
        new_blog = BlogModel()
        new_blog.title = params["title"]
        new_blog.content = params["content"]
        new_blog.slug = params["slug"]
        db.session.add(new_blog)
        db.session.commit()
        return model_obj_to_dict(new_blog)

    """ blog get api"""
    @ResourceFilter(methods=["get"])
    def get_list(self, params):
        result = []
        blog_rows = BlogModel.query.all()
        for b in blog_rows:
            result.append(model_obj_to_dict(b))
        return result

    @ResourceFilter("/<int:blog_id>", methods=["get"])
    def get_one(self, blog_id):
        pass

api.add_resource("/blog", Blog)
