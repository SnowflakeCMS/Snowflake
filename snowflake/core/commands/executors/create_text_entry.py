# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/06/25

from ..factory import CommandFactory

from snowflake.core.models.entries.text_entry import TextEntry


@CommandFactory.executor
class CreateTextEntry(object):
    def __init__(self, queue, cmd_obj):
        self.command = cmd_obj
        self.command_queue = queue

    def exec(self, guid, content_format, title, content):
        new_article = TextEntry()
        new_article.title = title
        new_article.guid = guid
        new_article.content_format = content_format
        new_article.content = content
