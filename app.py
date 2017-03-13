# -*- encoding: utf-8 -*-
import os

from flask_migrate import Migrate

from cfblog2 import front, core, api, db
from cfblog2.core.app import CoreApp
from cfblog2.tools import cfbm


def create_app(conf_preset, conf_override):
    basedir = os.path.abspath(os.path.dirname(__file__))
    new_app = CoreApp(db, basedir, "cfblog2", static_folder=None)
    new_app.config
    # TODO 使用Config配置创建
    new_app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    new_app.debug = True
    db.init_app(new_app)

    # blue print init
    core.init(new_app)

    api.init(new_app, url_prefix="/api")

    front.init(new_app)

    Migrate(new_app, db)

    cfbm.init(new_app)
    return new_app

create_app()


