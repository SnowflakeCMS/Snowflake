#
from cfblog2.restful.flask import FlaskBlueprint

api = FlaskBlueprint("api", __name__)


def init(app):
    from . import auth
