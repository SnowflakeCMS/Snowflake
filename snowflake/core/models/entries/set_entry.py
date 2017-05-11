# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/5/12


from snowflake import db
from .base import Entry, EntryType


class EntrySet(Entry):
    """ Category model
    """
    __table__name = "set"
    id = db.Column(db.Integer, db.ForeignKey("entry.id"), primary_key=True)
    name = db.Column(db.String(length=256))
    __mapper_args__ = {
        "polymorphic_identity": EntryType.EntrySet
    }