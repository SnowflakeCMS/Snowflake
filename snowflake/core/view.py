# -*- encoding:utf-8 -*-
from flask import render_template
from flask.views import View
from werkzeug.exceptions import abort


class CoreView(View):

    def dispatch_request(self):
        raise NotImplementedError()

    # noinspection PyMethodMayBeStatic
    def abort_with_code(self, code, *args, **extra):
        abort(code, *args, **extra)

    def render_template(self, tpl_name, **kwargs):
        predefined_variable = {
            "title": "中文标题"
        }
        predefined_variable.update(**kwargs)

        return render_template(tpl_name, **predefined_variable)
