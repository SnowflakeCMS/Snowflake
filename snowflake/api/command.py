# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/6/25
from snowflake.core.commands import CommandFactory
from snowflake.restful.resource import ResourceFilter
from . import APICallException, APICore, api


class ArticleException(APICallException):
    pass


@api.resource("/command")
class Command(APICore):
    name = "Command"
    desc = "Command API"
    need_auth = True

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    @ResourceFilter(methods=["post"])
    def execute(self, params):
        cmd_array = params["commands"]
        CommandFactory.create_queue(cmd_array)