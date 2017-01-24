# -*- encoding: utf-8 -*-
# author:Shane Yao
# create@:2017/1/24
# Migration tools from other blog to cfblog2

import pymysql
from . import config

def debug_log(fmt, *args):
    print(fmt % args)


class ContentFetcher(object):
    def __init__(self):
        super(ContentFetcher, self).__init__()

    def prepare(self):
        raise NotImplementedError


class TypechoFetcher(ContentFetcher):
    def __init__(self, conf):
        super(TypechoFetcher, self).__init__()
        self._mysql_conf = dict(conf)
        self._mysql_connection = None

    def prepare(self):
        debug_log("fetcher prepare")
        try:
            self._mysql_conf = pymysql.connect(**self._mysql_conf)
        except pymysql.OperationalError as e:
            pass



class BlogMigrate(object):
    def __init__(self, fetcher):
        self._fetcher = fetcher

    def start(self):
        debug_log("------------------>start ")
        self._fetcher.prepare()


def main():
    fetcher = TypechoFetcher(config.fetcher)
    bm = BlogMigrate(fetcher)
    bm.start()


if __name__ == "__main__":
    main()

