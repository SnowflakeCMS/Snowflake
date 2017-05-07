# -*- encoding: utf-8 -*-

from http import HTTPStatus
from flask import make_response
from flask.globals import request
from flask import current_app, Blueprint, abort


class APIManager(Blueprint):
    """Flask support of restful
    """

    def __init__(self, *args, **kwargs):
        super(APIManager, self).__init__(*args, **kwargs)

    def get_resource_register(self, res_cls):
        def __internal_register(rule, handle_func_name, methods, **options):
            self.add_url_rule(rule, methods=methods,
                              view_func=lambda *args, **kwargs: self.dispatch_request(res_cls,
                                                                                      handle_func_name,
                                                                                      *args,
                                                                                      **kwargs),
                              endpoint="%s#%s" % (res_cls.name, handle_func_name),
                              strict_slashes=True,
                              **options)
        return __internal_register

    def dispatch_request(self, res_cls, handle_func_name, *args, **kwargs):
        method_name = request.method.lower()
        res = res_cls(current_app.logger, self)
        content = request.get_data(as_text=True)
        content_mime_type = request.mimetype
        result_mime_type, result_str = res.dispatch_call(handle_func_name, method_name, content,
                                                         content_mime_type, *args, **kwargs)
        response = make_response(result_str)
        response.mime_type = result_mime_type
        return response

    @staticmethod
    def abort_403(msg=""):
        abort(HTTPStatus.UNAUTHORIZED, msg)

