import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

__app_instance = None


class CoreApp(object):
    def __init__(self):
        local_app = Flask(__name__)
        basedir = os.path.abspath(os.path.dirname(__file__))
        local_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "..", "db.sqlite")
        local_app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
        local_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        self._app = local_app

        local_db = SQLAlchemy(self._app)
        self._db = local_db

    def get_flask_app(self):
        return self._app

    def get_db(self):
        return self._db


def get_or_create_app():
    global __app_instance
    if __app_instance is None:
        __app_instance = CoreApp()
    return __app_instance
