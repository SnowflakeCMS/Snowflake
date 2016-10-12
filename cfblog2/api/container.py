# -*- encoding: utf-8 -*-
from cfblog2 import db
from cfblog2.api import APICallException, APICore
from cfblog2.core.utils import model_obj_to_dict
from cfblog2.restful.resource import ResourceFilter
from cfblog2.core.models import Container as ContainerModel
from . import api


class ContainerException(APICallException):
    pass


@api.resource("/container")
class Container(APICore):
    name = "Container"
    desc = "Container API"
    need_auth = False

    def __init__(self, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)

    # Get category list
    @ResourceFilter(methods=["get"])
    def retrieve_all(self, params):
        cat_rows = ContainerModel.query.all()
        result = []
        for c in cat_rows:
            result.append(model_obj_to_dict(c))
        return result

    @ResourceFilter(methods=["post"])
    def create(self, params):
        name = params["name"]
        new_cat = ContainerModel()
        new_cat.name = name
        db.session.add(new_cat)
        db.session.commit()
        return model_obj_to_dict(new_cat)

    @ResourceFilter("/<int:category_id>", methods=["patch"])
    def update_one(self, params, category_id):
        name = params["name"]
        cat = self.query_by_id(category_id).first()
        if cat is None:
            return None
        cat.name = name
        db.session.commit()
        return model_obj_to_dict(cat)

    @ResourceFilter("/<int:category_id>", methods=["delete"])
    def delete_one(self, params, category_id):
        delete_count = self.query_by_id(category_id).delete()
        return {"delete_count": delete_count}

    @ResourceFilter("/<int:category_id>", methods=["get"])
    def retrieve_one(self, params, category_id):
        cat = self.query_by_id(category_id).first()
        if cat is None:
            return None
        return model_obj_to_dict(cat)

    # noinspection PyMethodMayBeStatic
    def query_by_id(self, category_id):
        return ContainerModel.query.filter_by(id=category_id)
