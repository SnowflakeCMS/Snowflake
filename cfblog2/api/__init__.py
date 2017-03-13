# -*- encoding: utf-8 -*-

from cfblog2.restful import Resource, ResourceManager
from cfblog2.restful.supports.flask import FlaskSupport
from .ret_code import RetCode

flask_app = FlaskSupport("api", __name__)
api = ResourceManager(flask_app)


class APICallException(Exception):
    def __init__(self, code, **kwargs):
        super(APICallException, self).__init__()
        self._rtc = code
        self._c = code.get_code()
        self._m = code.get_msg().format(**kwargs)

    def get_code_msg(self):
        return self._c, self._m


class APICore(Resource):

    auth_method = None

    def __init__(self, *args, **kwargs):
        super(APICore, self).__init__(*args, **kwargs)

    def exec(self, *args, **kwargs):
        result = {
            "code": RetCode.OK.get_code(),
            "msg": RetCode.OK.get_msg(),
            "ret": None
        }

        try:
            ret = super(APICore, self).exec(*args, **kwargs)
            result["ret"] = ret
        except APICallException as ce:
            result["code"], result["msg"] = ce.get_code_msg()
        return result

    # noinspection PyMethodMayBeStatic
    def auth(self, params):
        if params is None:
            return False
        token = params.get("token", None)
        if token is None:
            return False
        return APICore.auth_method(token)


def init(app, url_prefix):
    # from . import auth, article, container
    from . import auth, article
    auth.set_config(app.secret_key, 7200)
    APICore.auth_method = auth.auth_method
    app.register_blueprint(flask_app, url_prefix=url_prefix)
