# -*- encoding:utf-8 -*-
from itsdangerous import TimedJSONWebSignatureSerializer
from cfblog2.core.models import User
from cfblog2.restful.types import String, Password
from . import api, APIBase, APICallException, RetCode


class AuthException(APICallException):
    pass


class Auth(APIBase):
    restful_method = {"post"}
    name = "Auth"
    desc = "System auth API"
    key = None
    expires_sec = 0

    def __init__(self, *args, **kwargs):
        super(Auth, self).__init__(*args, **kwargs)

    """Auth API"""
    def post(self, params, *args, **kwargs):
        p_username = params["username"]
        p_password = params["password"]

        user = User.query.filter_by(username=p_username, password=p_password).first()
        if user is None:
            self._logger.debug("Auth failed, username=%s", p_username)
            raise AuthException(RetCode.AUTH_PWD_USER_NOT_MATCH, username=p_username)

        s = TimedJSONWebSignatureSerializer(self.key, expires_in=self.expires_sec)
        token = s.dumps({"u": p_username}).decode("utf-8")
        self._logger.debug("-------------Token:%s", token)
        return token


def set_config(key, expires_sec=300):
    Auth.key = key
    Auth.expires_sec = expires_sec


api.add_resource("/auth", Auth)
