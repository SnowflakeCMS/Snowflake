# -*- encoding: utf-8 -*-


from flask_migrate import Migrate

from snowflake import core, api, db
from snowflake.portal.app import PortalApp
from snowflake.tools import cfbm


def create_app(py_conf_path):

    portal_app = PortalApp(py_conf_path, db, __name__)
    # blue print init
    core.init(portal_app)

    api.init(portal_app)

    Migrate(portal_app, db)

    cfbm.init(portal_app)
    return portal_app


app = create_app("app.config.py")


