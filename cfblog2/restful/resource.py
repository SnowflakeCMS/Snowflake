# -*- encoding: utf-8 -*-

import json


class ResourceFilter(object):
    def __init__(self, sub_pattern="", methods=[], need_auth=None):
        self.sub_pattern_ = sub_pattern
        self.methods_ = methods
        self.handle_func_ = None
        self.need_auth_ = need_auth
        self.name_ = None

    def __call__(self, handle_func):
        self.handle_func_ = handle_func
        return self

    def get_name(self):
        return self.name_

    def set_name(self, name):
        self.name_ = name

    def get_handle_func(self):
        return self.handle_func_

    def get_sub_pattern(self):
        return self.sub_pattern_

    def get_methods(self):
        return self.methods_

    def set_need_auth_from_resource(self, need_auth):
        if self.need_auth_ is not None:
            return
        self.need_auth_ = need_auth

    def get_need_auth(self):
        return self.need_auth_ is True


class ResourceMeta(type):
    def __init__(cls, name, bases, attrs):
        type.__init__(cls, name, bases, attrs)
        cls._filters = set()
        cls.restful_method = set()
        for k, v in attrs.items():
            if isinstance(v, ResourceFilter):
                cls._filters.add(v)
                cls.restful_method.update(v.get_methods())
                v.set_name(k)
                v.set_need_auth_from_resource(cls.need_auth)

    def __call__(cls, *args, **kwargs):
        return type.__call__(cls, *args, **kwargs)

    def __setattr__(cls, key, value):
        type.__setattr__(cls, key, value)


class Resource(object, metaclass=ResourceMeta):
    """Restful resource base class"""
    restful_method = None
    name = "DefaultName"
    desc = "Resource base class"
    need_auth = False
    # Fill by meta-class
    _filters = None

    def __init__(self, logger, app):
        self.logger_ = logger
        self.app_ = app

    def parse_params(self, content, content_mime_type):
        self.logger_.debug("-----------%s", content)
        raw_params = None
        if content_mime_type == "application/json":
            raw_params = json.loads(content)
        elif content_mime_type == "" or content_mime_type == "text/plain":
            raw_params = None
        else:
            self.logger_.warn("Unsupported content type:%s", content_mime_type)
        return raw_params

    def parse_result(self, result):
        return "application/json", json.dumps(result, ensure_ascii=False)

    def exec(self, handle_func_name, method_type, params, content_mime_type, *args, **kwargs):
        method = getattr(self, handle_func_name, None)
        assert method is not None, "Method should not be none"
        handle_func = method.get_handle_func()
        is_need_auth = method.get_need_auth()

        if is_need_auth and not self.auth(params):
            return self.app_.abort_403("Resource auth failed")

        # TODO Check mime type and call decode method in Resource
        result = handle_func(self, params, *args, **kwargs)
        return result

    def dispatch_call(self, handle_func_name, method_type, content, content_mime_type, *args, **kwargs):
        params = self.parse_params(content, content_mime_type)
        result = self.exec(handle_func_name, method_type, params, content_mime_type, *args, **kwargs)
        result_mime_type, result_str = self.parse_result(result)

        return result_mime_type, result_str

    def log_debug(self, *args, **kwargs):
        return self.logger_.debug(*args, **kwargs)

    def log_info(self, *args, **kwargs):
        return self.logger_.info(*args, **kwargs)

    def log_error(self, *args, **kwargs):
        return self.logger_.error(*args, **kwargs)

    # Override
    def auth(self, params):
        return True

    @classmethod
    def get_filters(cls):
        return cls._filters
