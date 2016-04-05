# -*- encoding: utf-8 -*-

from .app import get_or_create_app
_db = get_or_create_app().get_db()


class Setting(_db.Model):
    """ SettingModels """
    __tablename__ = "setting"
    id = _db.Column(_db.Integer, primary_key=True)


class Content(_db.Model):
    """ ContentModel """
    __tablename__ = "content"
    id = _db.Column(_db.Integer, primary_key=True)


class Page(Content):
    pass
