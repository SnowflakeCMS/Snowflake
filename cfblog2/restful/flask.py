# -*- encoding: utf-8 -*-

from http import HTTPStatus
from flask import make_response
from flask.views import View
from flask.globals import request
from flask import Flask, current_app, Blueprint, abort
from .resource import Resource


class FlaskResource(View):

    def __init__(self, res_cls):
        super(View, self).__init__()
        current_app.logger.debug("-------------->")
        self.methods = res_cls.restful_method
        self._res = res_cls(current_app.logger)
        self._res_cls = res_cls

    def dispatch_request(self, *args, **kwargs):
        method_name = request.method.lower()
        if method_name not in self._res_cls.restful_method:
            abort(HTTPStatus.BAD_REQUEST, "Unsupported http method:%r" % request.method)

        content = request.get_data(as_text=True)
        content_mime_type = request.mimetype
        result_mime_type, result_str = self._res.dispatch_call(method_name, content, content_mime_type)
        response = make_response(result_str)
        response.mime_type = result_mime_type
        return response


class FlaskBlueprint(Blueprint):
    """Flask support of restful
    """
    def __init__(self, *args, **kwargs):
        super(FlaskBlueprint, self).__init__(*args, **kwargs)

    def add_resource(self, rule, res_cls):
        # TODO check res_cls is subclass of FlaskResource
        self.add_url_rule(rule, methods=res_cls.restful_method,
                          view_func=FlaskResource.as_view(res_cls.name, res_cls))
