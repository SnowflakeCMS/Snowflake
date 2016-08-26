# -*- encoding: utf-8 -*-

from http import HTTPStatus
from flask import make_response
from flask.views import View
from flask.globals import request
from flask import Flask, current_app, Blueprint, abort
from cfblog2.restful.resource import Resource


class FlaskSupport(Blueprint):
    """Flask support of restful
    """

    def __init__(self, *args, **kwargs):
        super(FlaskSupport, self).__init__(*args, **kwargs)
        self.after_request(self.on_after_each_request)

    def get_url_register(self, res_cls):
        methods = res_cls.restful_method
        view_func = FlaskResource.as_view(res_cls.name, res_cls)

        def __internal_register(rule, **options):
            self.add_url_rule(rule, methods=methods,
                              view_func=view_func, **options)

        return __internal_register

    def dispatch_request(self, *args, **kwargs):
        method_name = request.method.lower()
        if method_name not in self._res_cls.restful_method:
            abort(HTTPStatus.BAD_REQUEST, "Unsupported http method:%r" % request.method)

        res = self._res_cls(current_app.logger)
        content = request.get_data(as_text=True)
        content_mime_type = request.mimetype
        current_app.logger.debug("-!!!--------------->%s,%s", args, kwargs)
        result_mime_type, result_str = res.dispatch_call(method_name, content, content_mime_type, *args, **kwargs)
        response = make_response(result_str)
        response.mime_type = result_mime_type
        current_app.logger.debug("response:%s", response)
        return response

    # noinspection PyMethodMayBeStatic
    def on_after_each_request(self, response):
        # 临时处理跨域
        h = response.headers
        h["Access-Control-Allow-Origin"] = "*"
        h["Access-Control-Max-Age"] = 21600
        if "Allow" in h:
            h["Access-Control-Allow-Methods"] = h["Allow"]
        h["Access-Control-Allow-Headers"] = "Content-Type"
        return response
