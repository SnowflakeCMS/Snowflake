# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/5/7

import enum
import os

from flask import Flask, request
from snowflake.core import app_config
from snowflake.core.settings import Settings


# implements using flask
class PortalApp(Flask):
    class CoreSettingEnum(enum.Enum):
        title = "core.title"
        subtitle = "core.subtitle"

    def __init__(self, py_conf_path, db, *args, **kwargs):
        super(PortalApp, self).__init__(*args, **kwargs)
        # snowflake configure, with `SNOWFLAKE_` prefix
        self.snowflake_config = None
        self._db = db
        self._api_manager = None
        self._migrate_tool = None

        self.load_conf_from_py(py_conf_path)
        self._db.init_app(self)
        self.before_request(self._before_each_request)

    def load_conf_from_py(self, py_conf_path):
        flask_config = self.config
        root_path = self.root_path
        flask_config.from_pyfile(os.path.join(root_path, py_conf_path))
        snowflake_conf = flask_config.get_namespace("SNOWFLAKE_", lowercase=False)
        preset = snowflake_conf.get("PRESET")
        preset_conf = app_config.create_config(preset, root_path)
        flask_config.from_object(preset_conf)
        self.snowflake_config = snowflake_conf

    def set_api_manager(self, api_manager, auth_module):
        self._api_manager = api_manager
        api_prefix = self.snowflake_config.get("API_PREFIX", None)
        if api_prefix is None:
            self.register_blueprint(api_manager)
        else:
            self.register_blueprint(api_manager, prefix=api_prefix)
        auth_module.set_config(self.get_secret_key(), 7200)

    def get_secret_key(self):
        return self.secret_key

    def _before_each_request(self):
        request.settings = Settings()


