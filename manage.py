# -*- encoding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand, Migrate
from cfblog2.core.app import get_or_create_app
from cfblog2 import front, admin


if __name__ == "__main__":
    core_app = get_or_create_app()
    # blue print init
    front.init(core_app)
    flask_app = core_app.get_flask_app()
    flask_app.debug = True
    sql_db = core_app.get_db()

    manager = Manager(flask_app)
    migrate = Migrate(flask_app, sql_db)
    manager.add_command("db", MigrateCommand)
    manager.run()
