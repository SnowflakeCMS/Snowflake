# -*- encoding: utf-8 -*-

import json


class ResourceMeta(type):
    def __init__(cls, name, bases, attrs):
        type.__init__(cls, name, bases, attrs)
        cls._unbound_params = {}

    def __call__(cls, *args, **kwargs):
        return type.__call__(cls, *args, **kwargs)

    def __setattr__(cls, key, value):
        type.__setattr__(cls, key, value)


class Resource(object, metaclass=ResourceMeta):
    """Restful resource base class"""
    restful_method = {"get", "post", "delete", "head", "patch"}

    name = "DefaultName"
    desc = "Resource base class"

    def __init__(self, logger):
        self._logger = logger

    def parse_params(self, content, content_mime_type):
        assert content_mime_type == "application/json", "Unsupported content type"
        raw_params = json.loads(content)
        return raw_params

    def parse_result(self, result):
        return "application/json", json.dumps(result)

    def exec(self, method_type, params, *args, **kwargs):
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
