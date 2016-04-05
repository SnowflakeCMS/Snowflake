# -*- encoding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand, Migrate
from cfblog2.core.app import CoreApp
from cfblog2 import front, admin, db


if __name__ == "__main__":

    app = CoreApp(__name__)
    app.debug = True
    db.init_app(app)

    # blue print init
    front.init(app)
    app.register_blueprint(front.front)

    admin.init(app)
    app.register_blueprint(admin.admin, url_prefix="/admin")

    manager = Manager(app)
    migrate = Migrate(app, db)
    manager.add_command("db", MigrateCommand)
    manager.run()
