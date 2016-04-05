import enum
import os
from flask import Flask


class CoreApp(Flask):
    class CoreSettingEnum(enum.Enum):
        title = "core.title"
        subtitle = "core.subtitle"

    def __init__(self, *args, **kwargs):
        super(CoreApp, self).__init__(*args, **kwargs)
        basedir = os.path.abspath(os.path.dirname(__file__))
        self.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "..", "db.sqlite")
        self.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
        self.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    def get_flask_app(self):
        return self._app

    def get_model(self, tbl_name):
        """ Get model class with specify name
        :param tbl_name: Table name of model
        :return: Model class
        """
        return self._db.Model.metadata.tables.get(tbl_name, None)

    def get_setting(self, enum):
        # For avoid import circle
        setting_model = self.get_model("setting")
