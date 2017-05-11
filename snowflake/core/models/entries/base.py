# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/5/12

import enum
import datetime
from snowflake import db


class EntryType(enum.IntEnum):
    Base = 1
    Text = 2
    EntrySet = 3
    Comment = 4


class Entry(db.Model):
    """ BaseEntry
    """
    __tablename__ = "entry"
    id = db.Column(db.Integer, primary_key=True)
    entry_type = db.Column(db.Enum(EntryType))
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    __mapper_args__ = {
        'polymorphic_identity': EntryType.Base,
        'polymorphic_on': entry_type
    }
