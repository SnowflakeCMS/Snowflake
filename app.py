# -*- encoding: utf-8 -*-
import os

from flask_migrate import Migrate
from cfblog2 import front, core, api, db
from cfblog2.core.app import CoreApp
from cfblog2.tools import cfbm


def create_app(py_conf_path):

    new_app = CoreApp(py_conf_path, db, __name__, static_folder=None)

    db.init_app(new_app)

    # blue print init
    core.init(new_app)

    api.init(new_app, url_prefix="/api")

    front.init(new_app)

    Migrate(new_app, db)

    cfbm.init(new_app)
    return new_app


app = create_app("app_config.py")


