# -*- encoding: utf-8 -*-

import enum
import pickle

from cfblog2 import db


class Setting(db.Model):
    class TypeEnum(enum.Enum):
        STRING = "str"
        PICKLE = "pik"
        PYTHON = "pyc"
    """ SettingModels """
    __tablename__ = "setting"
    id = db.Column(db.String(length=256), primary_key=True)
    type = db.Column(db.String(length=16))
    value = db.Column(db.UnicodeText)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_string_value(self, value):
        self.value = value
        self.type = Setting.TypeEnum.STRING

    def set_object_value(self, obj):
        # TODO
        pass


class Blog(db.Model):
    """ BlogModel
    """
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(length=256))
    title = db.Column(db.Unicode(length=512))
    content = db.Column(db.UnicodeText)


class Comment(db.Model):
    """ CommentModel
    """
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)


class Category(db.Model):
    """ Category model
    """
    __table__name = "category"
    id = db.Column(db.Integer, primary_key=True)
