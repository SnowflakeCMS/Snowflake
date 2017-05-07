# -*- encoding: utf-8 -*-


class ResourceManager(object):
    def __init__(self, app):
        self.app_ = app
        self.resources_by_url_ = {}

    def resource(self, url):
        assert url not in self.resources_by_url_

        def __decorator_func(cls):
            register = self.app_.get_resource_register(cls)
            res_filters = cls.get_filters()

            for res_filter in res_filters:
                register(rule="%s%s" % (url, res_filter.get_sub_pattern()),
                         handle_func_name=res_filter.get_name(),
                         methods=res_filter.get_methods())
            self.resources_by_url_[url] = cls
            return cls
        return __decorator_func
