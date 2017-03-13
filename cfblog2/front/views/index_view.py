# -*- encoding: utf-8 -*-
from flask import render_template, request

from cfblog2.core.models import ArticleEntry as ArticleModel
from cfblog2.core.view import CoreView
from cfblog2.core.debug import log_debug


class IndexView(CoreView):
    methods = ["GET"]

    def __init__(self, *args, **kwargs):
        super(IndexView, self).__init__(*args, **kwargs)

    def dispatch_request(self):
        blog_list = ArticleModel.query.all()
        context = {
            "blog_list": blog_list
        }
        log_debug("Context:%s, %s", context, request.settings)
        return render_template("front_index.html", title="博客中文标题", **context)


