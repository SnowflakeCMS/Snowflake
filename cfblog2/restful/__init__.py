# -*- encoding:utf-8 -*-
from flask import Blueprint
from flask.globals import request
from flask.views import View


class Resource(View):
    """Restful resource base class"""

    # Standard method of restful API
    methods = ["GET", "PUT"]
    rest_standard_method = {"get", "post", "delete", "head", "patch"}

    def __init__(self):
        super(Resource, self).__init__()

    def dispatch_request(self, *args, **kwargs):
        method_name = request.method.lower()
        if method_name not in Resource.rest_standard_method:
            raise NotImplementedError("Unsupported http method:%r" % request.method)

        method = getattr(self, method_name, None)
        if method is None:
            raise NotImplementedError("Resource not implements this method")

        print("----------------->", request.mimetype)
        return method(*args, **kwargs)


class RestfulBlueprint(Blueprint):
    pass
