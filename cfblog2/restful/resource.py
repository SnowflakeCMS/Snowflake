# -*- encoding: utf-8 -*-


class ResourceMeta(type):

    def __init__(cls, name, bases, attrs):
        print("---------init---", cls, name, bases, attrs)
        type.__init__(cls, name, bases, attrs)
        cls._unbound_params = {}

    def __call__(cls, *args, **kwargs):
        print("_______CALL_____", args, kwargs)
        return type.__call__(cls, *args, **kwargs)

    def __setattr__(cls, key, value):
        print("__setattr__", key, value)
        type.__setattr__(cls, key, value)


class Resource(object, metaclass=ResourceMeta):
    """Restful resource base class"""
    rest_standard_method = {"get", "post", "delete", "head", "patch"}
    name = "DefaultName"

    def __init__(self):
        super(Resource, self).__init__()

    def decode_params(self, params):
        pass

    def encode_result(self, result):
        pass
