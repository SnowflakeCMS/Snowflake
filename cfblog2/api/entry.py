# -*- encoding: utf-8 -*-
from cfblog2 import db
from cfblog2.api import APICore, APICallException
from cfblog2.core.models import Entry as EntryModel
from cfblog2.core.utils import model_obj_to_dict
from cfblog2.restful.resource import ResourceFilter
from . import api


class EntryException(APICallException):
    pass


@api.resource("/entry")
class Entry(APICore):
    name = "Entry"
    desc = "Entry resource api"
    need_auth = False

    def __init__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)

    """Post entry api"""
    @ResourceFilter(methods=["post"])
    def create(self, params):
        # TODO use param validator
        new_entry = EntryModel()
        new_entry.title = params["title"]
        new_entry.content = params["content"]
        new_entry.slug = params["slug"]
        db.session.add(new_entry)
        db.session.commit()
        return model_obj_to_dict(new_entry)

    """ entry get api"""
    @ResourceFilter(methods=["get"])
    def retrieve_all(self, params):
        result = []
        rows = EntryModel.query.all()
        for b in rows:
            result.append(model_obj_to_dict(b))
        return result

    @ResourceFilter("/<int:entry_id>", methods=["get"])
    def retrieve_one(self, params, entry_id):
        entry = self.query_by_id(entry_id).first()
        if entry is None:
            return None
        else:
            return model_obj_to_dict(entry)

    @ResourceFilter("/<int:entry_id>", methods=["delete"])
    def delete_one(self, params, entry_id):
        delete_count = self.query_by_id(entry_id).delete()
        db.session.commit()

        return {"count": delete_count}

    @ResourceFilter("/<int:entry_id>", methods=["patch"])
    def update_one(self, params, entry_id):
        entry = self.query_by_id(entry_id).first()
        if entry is None:
            return None

        entry.title = params["title"]
        entry.content = params["content"]
        entry.slug = params["slug"]
        db.session.commit()
        return model_obj_to_dict(entry)

    # noinspection PyMethodMayBeStatic
    def query_by_id(self, entry_id):
        return EntryModel.query.filter_by(id=entry_id)
