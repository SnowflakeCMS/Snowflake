# -*- encoding: utf-8 -*-

from cfblog2.restful import Resource, ResourceManager
from cfblog2.restful.supports.flask import FlaskSupport
from .ret_code import RetCode

flask_app = FlaskSupport("api", __name__)
api = ResourceManager(flask_app)


class APICallException(Exception):
    def __init__(self, code, *args, **kwargs):
        super(APICallException, self).__init__()
        self._rtc = code
        self._c = code.get_code()
        self._m = code.get_msg().format(**kwargs)

    def get_code_msg(self):
        return self._c, self._m


class APIBase(Resource):
    name = "APIBase"
    desc = "cfblog2 API base class"

    def __init__(self, *args, **kwargs):
        super(APIBase, self).__init__(*args, **kwargs)

    def exec(self, method_type, params, *args, **kwargs):
        result = {
            "code": RetCode.OK.get_code(),
            "msg": RetCode.OK.get_msg(),
            "ret": None
        }

        try:
            ret = super(APIBase, self).exec(method_type, params, *args, **kwargs)
            result["ret"] = ret
        except APICallException as ce:
            result["code"], result["msg"] = ce.get_code_msg()
        return result


def init(app, url_prefix):
    from . import auth, blog
    auth.set_config(app.secret_key)

    app.register_blueprint(flask_app, url_prefix=url_prefix)
