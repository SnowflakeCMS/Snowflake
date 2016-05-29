# -*- encoding: utf-8 -*-

from .ret_code import RetCode
from cfblog2.restful import Resource
from cfblog2.restful.flask import FlaskBlueprint, FlaskResource

api = FlaskBlueprint("api", __name__)


class APICallException(Exception):
    def __init__(self, code, *args, **kwargs):
        super(APICallException, self).__init__(*args, **kwargs)
        self._rtc = code
        self._c = code.get_code()
        self._m = code.get_msg()

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
            ret = None
            result["code"], result["msg"] = ce.get_code_msg()
        return result


def init(app):
    from . import auth
    auth.set_config(app.secret_key)
