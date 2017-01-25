# -*- encoding: utf-8 -*-
# author:Shane Yao
# create@:2017/1/25
# Migration class

import pymysql

from cfblog2 import db
from cfblog2.core.models import ArticleEntry as ArticleModel


class DefaultLogger(object):
    @staticmethod
    def _log(prefix, fmt, *args):
        print((prefix + fmt) % args)

    def debug(self, fmt, *args):
        self._log("[DEBUG]", fmt, *args)

    def info(self, fmt, *args):
        self._log("[INFO]", fmt, *args)

    def error(self, fmt, *args):
        self._log("[ERROR]", fmt, *args)

    def exception(self, fmt, *args):
        self._log("[EXCEPTION]", fmt, *args)
        self.last_except()

    def last_except(self):
        import sys
        c = sys.exc_info()
        import traceback
        traceback.print_exception(*c)


class ContentFetcher(object):
    def __init__(self):
        super(ContentFetcher, self).__init__()

    def prepare(self):
        raise NotImplementedError

    def tear_down(self):
        raise NotImplementedError

    def get_all_articles(self):
        raise NotImplementedError


class TypechoFetcher(ContentFetcher):
    def __init__(self, conf):
        super(TypechoFetcher, self).__init__()
        self.logger = DefaultLogger()
        self.mysql_conf = dict(conf)
        self.mysql_connection = None
        self._tbl_prefix = "typecho_"
        self._tbl_suffix = ""

    def _get_table_name(self, name):
        return self._tbl_prefix + name + self._tbl_suffix

    def prepare(self):
        self.logger.info("Fetcher prepare")
        try:
            self.mysql_connection = pymysql.connect(**self.mysql_conf)
        except pymysql.OperationalError:
            self.logger.exception("Could not connect to mysql")

    def get_all_articles(self):
        cursor = self.mysql_connection.cursor()
        cursor.execute("select title, text, slug from %s" % self._get_table_name("contents"))
        return cursor.fetchall()

    def tear_down(self):
        self.mysql_connection.close()


class BlogMigrate(object):
    def __init__(self, fetcher):
        self.logger = DefaultLogger()
        self.fetcher = fetcher

    def start(self):
        self.logger.info("Blog migrate start")
        self.fetcher.prepare()
        self._migrate_articles()

    def finish(self):
        self.logger.info("Blog migrate finish")

    def tear_down(self):
        self.logger.info("Blog migrate tear down")
        self.fetcher.tear_down()

    def _migrate_articles(self):
        self.logger.info("Start migrating articles")
        articles = self.fetcher.get_all_articles()
        for article in articles:
            self.logger.debug("---------Title:%s", article[2])
            a = ArticleModel()
            a.title = article[0]
            a.content = article[1]
            a.slug = article[2]
            a.content_format = ArticleModel.ArticleFormat.PlainText
            db.session.add(a)
            db.session.commit()



