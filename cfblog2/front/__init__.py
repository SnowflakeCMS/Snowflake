# -*- encoding:utf -8 -*-

from flask.blueprints import Blueprint

from .views.blog_view import BlogView
from .views.index_view import IndexView
from .utils import jinja_filters

front = Blueprint("front", __name__,
                  static_folder="static",
                  template_folder="templates")


def init(app):
    # TODO Maybe export url configure to root config?
    app.add_url_rule("/", view_func=IndexView.as_view("IndexView"))
    app.add_url_rule("/blog/<string:slug>/<int:blog_id>", view_func=BlogView.as_view("BlogView"))

    front.add_app_template_filter(jinja_filters.url_for_blog)
    front.add_app_template_filter(jinja_filters.url_for_theme)
    app.register_blueprint(front)
