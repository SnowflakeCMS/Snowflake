from flask.blueprints import Blueprint

core = Blueprint("core", __name__)


def init(app):
    from . import models
    app.register_blueprint(core)
