# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/5/12

import enum
from snowflake import db


class LinkingType(enum.IntEnum):
    Normal = 1
    Set = 2


class Linking(db.Model):
    """Represent one-way linking[form -> to]"""
    __tablename__ = "linking"
    id = db.Column(db.Integer, primary_key=True)
    rel_type = db.Column(db.Enum(LinkingType), default=LinkingType.Normal)
    rel_from = db.Column(db.Integer)
    rel_to = db.Column(db.Integer)

