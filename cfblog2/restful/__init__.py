# -*- encoding:utf-8 -*-
from flask import Blueprint
from flask.globals import request
from flask.views import View


class Resource(View):
    # Standard method of restful API
    rest_standard_method = {"get", "post", "delete", "head", "patch"}

    def __init__(self):
        super(Resource, self).__init__()

    def dispatch_request(self, *args, **kwargs):
        method_name = request.method.lower()
        print("-------------", method_name)
        if method_name not in Resource.rest_standard_method:
            raise NotImplementedError("Unsupported http method:%r" % request.method)

        method = getattr(self, method_name, None)
        if method is None:
            raise NotImplementedError("Resource not implements this method")

        return method(*args, **kwargs)


class RestfulBlueprint(Blueprint):
    pass
