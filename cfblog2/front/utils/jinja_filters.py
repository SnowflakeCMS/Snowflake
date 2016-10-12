# -*- encoding: utf-8 -*-


def url_for_blog(obj):
    return "/blog/%s/%d" % (obj.slug, obj.id)



