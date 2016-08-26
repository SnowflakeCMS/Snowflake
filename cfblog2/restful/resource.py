# -*- encoding: utf-8 -*-

import json


class ResourceFilter(object):
    def __init__(self, sub_patterns="", methods=[]):
        self.sub_patterns_ = sub_patterns
        self.methods_ = methods

        self.handle_func_ = None

    def __call__(self, handle_func):
        self.handle_func_ = handle_func
        return self

    def get_handle_func(self):
        return self.handle_func_


class ResourceMeta(type):
    def __init__(cls, name, bases, attrs):
        type.__init__(cls, name, bases, attrs)
        cls._unbound_params = {}
        cls._filters = set()

    def __call__(cls, *args, **kwargs):
        return type.__call__(cls, *args, **kwargs)

    def __setattr__(cls, key, value):
        if isinstance(value, ResourceFilter):
            cls._filters.add(value)
            type.__setattr__(cls, key, value.get_handle_func())
        else:
            type.__setattr__(cls, key, value)


class Resource(object, metaclass=ResourceMeta):
    """Restful resource base class"""
    restful_method = {"get", "post", "delete", "head", "patch"}

    name = "DefaultName"
    desc = "Resource base class"

    def __init__(self, logger):
        self.logger_ = logger

    def parse_params(self, content, content_mime_type):
        self.logger_.debug("-----------%s", content)
        raw_params = None
        if content_mime_type == "application/json":
            raw_params = json.loads(content)
        elif content_mime_type == "":
            raw_params = None
        else:
            self.logger_.warn("Unsupported content type:%s", content_mime_type)
        return raw_params

    def parse_result(self, result):
        return "application/json", json.dumps(result, ensure_ascii=False)

    def exec(self, method_type, params, content_mime_type, *args, **kwargs):
        method = getattr(self, method_type, None)
        assert method is not None, "Unimplemented method"

        # TODO Check mime type and call decode method in Resource
        result = method(params, *args, **kwargs)
        return result

    def dispatch_call(self, method_type, content, content_mime_type, *args, **kwargs):
        params = self.parse_params(content, content_mime_type)
        result = self.exec(method_type, params, content_mime_type, *args, **kwargs)
        result_mime_type, result_str = self.parse_result(result)

        return result_mime_type, result_str