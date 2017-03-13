import enum
import os

from flask import Flask, request
from . import app_config
from .settings import Settings


class CoreApp(Flask):
    class CoreSettingEnum(enum.Enum):
        title = "core.title"
        subtitle = "core.subtitle"

    def __init__(self, py_conf_path, db, *args, **kwargs):
        super(CoreApp, self).__init__(*args, **kwargs)
        # snowflake configure, with `SNOWFLAKE_` prefix
        self.snowflake_config = None
        self.load_conf_from_py(py_conf_path)

        self._db = db
        self.before_request(self._before_each_request)

    def load_conf_from_py(self, py_conf_path):
        self.config.from_pyfile(os.path.join(self.root_path, py_conf_path))
        snowflake_conf = self.config.get_namespace("SNOWFLAKE_", lowercase=False)
        preset = snowflake_conf.get("PRESET")
        preset_conf = app_config.create_config(preset, self.root_path)
        self.config.from_object(preset_conf)
        self.snowflake_config = snowflake_conf

    def _before_each_request(self):
        request.settings = Settings()


