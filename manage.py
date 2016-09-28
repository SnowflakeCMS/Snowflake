# -*- encoding: utf-8 -*-
import os

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

from cfblog2.core.app import CoreApp
from cfblog2 import front, admin, core, api, db


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = CoreApp(db, basedir, "cfblog2", static_folder=None)
    # TODO 使用Config配置创建
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.debug = True
    db.init_app(app)

    # blue print init
    core.init(app)

    api.init(app, url_prefix="/api")

    front.init(app)

    admin.init(app, url_prefix="/admin")

    manager = Manager(app)
    migrate = Migrate(app, db)
    manager.add_command("db", MigrateCommand)
    manager.run()
