# -*- encoding:utf-8 -*-
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature
from snowflake.core.models import User
from snowflake.restful.resource import ResourceFilter
from . import api, APICore, APICallException, RetCode


class AuthException(APICallException):
    pass


@api.resource("/auth")
class Auth(APICore):
    name = "Auth"
    desc = "System auth API"
    key = None
    expires_sec = 0

    def __init__(self, *args, **kwargs):
        super(Auth, self).__init__(*args, **kwargs)

    """Auth API"""
    @ResourceFilter("", methods=["post"])
    def post(self, params):
        p_username = params["username"]
        p_password = params["password"]

        user = User.query.filter_by(username=p_username, password=p_password).first()
        if user is None:
            self.log_info("Auth failed, username=%s", p_username)
            raise AuthException(RetCode.AUTH_PWD_USER_NOT_MATCH, username=p_username)

        s = TimedJSONWebSignatureSerializer(self.key, expires_in=self.expires_sec)
        token = s.dumps({"u": p_username}).decode("utf-8")
        return token


def set_config(key, expires_sec=300):
    Auth.key = key
    Auth.expires_sec = expires_sec


def auth_method(token):
    s = TimedJSONWebSignatureSerializer(Auth.key, expires_in=Auth.expires_sec)
    auth_dict = None
    try:
        auth_dict = s.loads(token)
    except BadSignature:
        pass

    if auth_dict is None:
        return False
    return True
