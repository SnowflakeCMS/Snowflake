# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/3/13


class Settings(object):
    def __init__(self):
        self._dirty = False
        self._update_dict = {}
        self._setting_dict = {}

    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def _lazy_load(self):
        pass

    def save(self):
        pass

