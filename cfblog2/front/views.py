from flask import render_template

from . import front


@front.route('/')
def index():
    return render_template("front_base.html", title="博客中文标题")
