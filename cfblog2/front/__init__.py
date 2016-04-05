# -*- encoding:utf -8 -*-

from flask.blueprints import Blueprint

front = Blueprint("front", __name__, static_folder="static", template_folder="templates")


# Blueprint's  initialize method
def init(core_app):
    from . import views
    core_app.get_flask_app().register_blueprint(front)

