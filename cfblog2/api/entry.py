# -*- encoding: utf-8 -*-
from cfblog2 import db
from cfblog2.api import APICore, APICallException
from cfblog2.core.models import Entry as EntryModel
from cfblog2.core.utils import model_obj_to_dict
from cfblog2.restful.resource import ResourceFilter
from . import api


class BlogException(APICallException):
    pass


@api.resource("/blog")
class Entry(APICore):
    name = "Blog"
    desc = "Blog resource api"
    need_auth = False

    def __init__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)

    """Post blog api"""
    @ResourceFilter(methods=["post"])
    def create(self, params):
        # TODO use param validator
        new_blog = EntryModel()
        new_blog.title = params["title"]
        new_blog.content = params["content"]
        new_blog.slug = params["slug"]
        db.session.add(new_blog)
        db.session.commit()
        return model_obj_to_dict(new_blog)

    """ blog get api"""
    @ResourceFilter(methods=["get"])
    def retrieve_all(self, params):
        result = []
        blog_rows = EntryModel.query.all()
        for b in blog_rows:
            result.append(model_obj_to_dict(b))
        return result

    @ResourceFilter("/<int:blog_id>", methods=["get"])
    def retrieve_one(self, params, blog_id):
        blog = self.query_by_id(blog_id).first()
        if blog is None:
            return None
        else:
            return model_obj_to_dict(blog)

    @ResourceFilter("/<int:blog_id>", methods=["delete"])
    def delete_one(self, params, blog_id):
        delete_count = self.query_by_id(blog_id).delete()
        db.session.commit()

        return {"count": delete_count}

    @ResourceFilter("/<int:blog_id>", methods=["patch"])
    def update_one(self, params, blog_id):
        blog = self.query_by_id(blog_id).first()
        if blog is None:
            return None

        blog.title = params["title"]
        blog.content = params["content"]
        blog.slug = params["slug"]
        db.session.commit()
        return model_obj_to_dict(blog)

    # noinspection PyMethodMayBeStatic
    def query_by_id(self, blog_id):
        return EntryModel.query.filter_by(id=blog_id)
