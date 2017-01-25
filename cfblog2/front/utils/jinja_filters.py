# -*- encoding: utf-8 -*-
from flask import url_for


def url_for_blog(obj):
    return "/blog/%d/%s" % (obj.id, obj.slug)


def url_for_theme(filename):
    return url_for("front.static", filename=filename)

def markdown_render(content):
    import CommonMark
    parser = CommonMark.Parser()
    ast = parser.parse(content)
    renderer = CommonMark.HtmlRenderer()
    html = renderer.render(ast)
    return html