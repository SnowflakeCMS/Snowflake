from flask.blueprints import Blueprint

core = Blueprint("core", __name__, static_folder="static", template_folder="templates")


def init(app):
    from . import models
