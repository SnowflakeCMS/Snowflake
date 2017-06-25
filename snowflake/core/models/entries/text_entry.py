# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/5/12

import enum
from snowflake import db
from .base import ContentEntry, EntryType


class TextEntry(ContentEntry):
    class TextFormat(enum.IntEnum):
        PlainText = 1
        Markdown = 2
        RestructuredText = 3

    """Text Entry"""
    __tablename__ = "text"
    id = db.Column(db.Integer, db.ForeignKey("entry.id"), primary_key=True)
    # slug = db.Column(db.String(length=256))
    title = db.Column(db.Unicode(length=512))
    content_format = db.Column(db.Enum(TextFormat))
    content = db.Column(db.UnicodeText)
    __mapper_args__ = {
        "polymorphic_identity": EntryType.Text
    }
