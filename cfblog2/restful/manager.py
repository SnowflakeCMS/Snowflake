# -*- encoding: utf-8 -*-


class ResourceManager(object):
    def __init__(self, app):
        self.app_ = app
        self.url_register_by_cls_ = {}

    def get_url_register(self, res_cls):
        register = self.url_register_by_cls_.get(res_cls, None)
        if register is None:
            register = self.app_.get_url_register(res_cls)
            self.url_register_by_cls_[res_cls] = register
        return register

    def add_resource(self, url, res_cls):
        register = self.get_url_register(res_cls)
