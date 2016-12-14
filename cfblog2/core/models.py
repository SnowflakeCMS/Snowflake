# -*- encoding: utf-8 -*-
import datetime
import enum
import pickle

from cfblog2 import db


class Setting(db.Model):
    """ SettingModels """
    class TypeEnum(enum.Enum):
        STRING = "str"
        PICKLE = "pik"
        PYTHON = "pyc"
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


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(length=128))
    password = db.Column(db.Unicode(length=128))


class Container(db.Model):
    """ Category model
    """
    __table__name = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=256))
    # blog = relationship("Blog", back_populates="category")


class EntryType(enum.IntEnum):
    BASE = 1
    ARTICLE = 2
    COMMENT = 3


class Entry(db.Model):
    """ BaseEntry
    """
    __tablename__ = "entry"
    id = db.Column(db.Integer, primary_key=True)
    entry_type = db.Column(db.Enum(EntryType))
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    __mapper_args__ = {
        'polymorphic_identity': EntryType.BASE,
        'polymorphic_on': entry_type
    }


class ArticleEntry(Entry):
    class ArticleFormat(enum.IntEnum):
        PlainText = 1
        Markdown = 2
        RestructuredText = 3

    """Article Entry"""
    __tablename__ = "article"
    id = db.Column(db.Integer, db.ForeignKey("entry.id"), primary_key=True)
    slug = db.Column(db.String(length=256))
    title = db.Column(db.Unicode(length=512))
    content_format = db.Column(db.Enum(ArticleFormat))
    content = db.Column(db.UnicodeText)
    __mapper_args__ = {
        "polymorphic_identity": EntryType.ARTICLE
    }


class CommentEntry(Entry):
    """Comment entry"""
    __tablename__ = "comment"
    id = db.Column(db.Integer, db.ForeignKey("entry.id"), primary_key=True)
    content = db.Column(db.UnicodeText)
    __mapper_args__ = {
        "polymorphic_identity": EntryType.COMMENT
    }


class Linking(db.Model):
    """Represent one-way linking[form -> to]"""
    __tablename__ = "linking"
    id = db.Column(db.Integer, primary_key=True)
    rel_from = db.Column(db.Integer)
    rel_to = db.Column(db.Integer)



