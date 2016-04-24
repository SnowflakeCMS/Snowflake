#
from cfblog2.restful import RestfulBlueprint

api = RestfulBlueprint("api", __name__)


def init(app):
    from . import auth
