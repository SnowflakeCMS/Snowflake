# -*- encoding: utf-8 -*-

from http import HTTPStatus
from flask.views import View
from flask.globals import request
from flask import Flask, current_app, Blueprint, abort
from .resource import Resource


class FlaskResource(View, Resource):
    def __init__(self):
        super(View, self).__init__()

    def dispatch_request(self, *args, **kwargs):
        method_name = request.method.lower()
        if method_name not in Resource.rest_standard_method:
            abort(HTTPStatus.BAD_REQUEST, "Unsupported http method:%r" % request.method)

        method = getattr(self, method_name, None)
        if method is None:
            abort(HTTPStatus.NOT_IMPLEMENTED, "Resource not implements this method")
        # TODO Check mime type and call decode method in Resource
        result = method(*args, **kwargs)
        # TODO Decode json
        return result


class FlaskBlueprint(Blueprint):
    """Flask support of restful
    """
    def __init__(self, *args, **kwargs):
        super(FlaskBlueprint, self).__init__(*args, **kwargs)

    def add_resource(self, rule, res_cls):
        # TODO check res_cls is subclass of FlaskResource
        self.add_url_rule(rule, view_func=res_cls.as_view(res_cls.name))
