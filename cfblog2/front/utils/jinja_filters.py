# -*- encoding: utf-8 -*-
from flask import url_for


def url_for_blog(obj):
    return "/blog/%s/%d" % (obj.slug, obj.id)


def url_for_theme(filename):
    return url_for("front.static", filename=filename)
