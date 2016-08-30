# -*- encoding: utf-8 -*-

from cfblog2.core.models import Blog


def url_for_blog(obj):
    return "/blog/%s/%d" % (obj.slug, obj.id)



