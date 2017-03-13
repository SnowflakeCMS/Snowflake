import enum
import os
from flask import Flask
from .models import Setting as SettingModel


class SettingCacheManager(object):
    def __init__(self):
        self._setting = {}


class CoreApp(Flask):
    class CoreSettingEnum(enum.Enum):
        title = "core.title"
        subtitle = "core.subtitle"

    def __init__(self, db, base_dir, *args, **kwargs):
        super(CoreApp, self).__init__(*args, **kwargs)
        self._project_base_dir = base_dir
        self.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "db.sqlite")
        self.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
        self.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        self._db = db

    def get_setting(self, enum):
        # For avoid import circle
        setting_model = self.get_model("setting")
