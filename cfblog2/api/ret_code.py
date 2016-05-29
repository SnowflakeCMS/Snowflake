# -*- encoding: utf-8 -*-

import enum


class RetCode(enum.Enum):
    """ General return code define"""
    OK = 0
    ERR_INTERNAL_START = 1
    ERR_INTERNAL_END = 999

    ERR_SYSTEM_START = 1000
    ERR_SYSTEM_END = 9999

    # API 相关错误从10000开始，每个API的错误号+100
    ERR_USER_START = 10000
    # AUTH Start with 10100
    AUTH_PWD_USER_NOT_MATCH = 10101

    def __str__(self):
        return MESSAGE.get(self, "No message")

    def get_desc(self):
        return str(self)

    def get_code(self):
        return self.value

    def get_msg(self):
        return str(self)


MESSAGE = {
    RetCode.OK: "OK",
    RetCode.AUTH_PWD_USER_NOT_MATCH: "Auth not match, user:{username}",
}
