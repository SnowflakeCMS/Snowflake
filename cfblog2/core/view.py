# -*- encoding:utf-8 -*-
from flask.views import View
from werkzeug.exceptions import abort


class CoreView(View):

    def dispatch_request(self):
        raise NotImplementedError()

    # noinspection PyMethodMayBeStatic
    def abort_with_code(self, code, *args, **extra):
        abort(code, *args, **extra)
