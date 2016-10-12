# -*- encoding: utf-8 -*-
from http import HTTPStatus

from flask import render_template

from cfblog2.core.models import Entry as EntryModel
from cfblog2.core.view import CoreView
from cfblog2.core.debug import log_info


class BlogView(CoreView):

    def dispatch_request(self, slug, blog_id):
        blog = EntryModel.query.filter_by(id=blog_id).first()
        if blog is None:
            log_info("Blog not found, id:%s, slug:%s", blog_id, slug)
            self.abort(HTTPStatus.NOT_FOUND)
        context = {
            "blog": blog,
        }

        return render_template("../themes/cfblog2/templates/front_blog.html", **context)
