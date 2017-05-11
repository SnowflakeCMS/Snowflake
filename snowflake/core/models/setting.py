# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/5/12

import enum
from snowflake import db


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


class SettingsManager(object):
    def __init__(self):
        self._dirty = False
        self._update_dict = {}
        self._setting_dict = {}

    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def _lazy_load(self):
        pass

    def save(self):
        pass

