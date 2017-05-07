# -*- encoding: utf-8 -*-


class TypeBase(object):
    def __init__(self, name, optional=True):
        self._name = name
        self._optional = optional


class Raw(TypeBase):
    def __init__(self, name, optional=True):
        super().__init__(name, optional=optional)

    def build(self, raw_value):
        return raw_value


class String(TypeBase):
    """Normal text field
    """
    pass


class DictionaryBody(object):
    def __init__(self):
        pass


class Dictionary(TypeBase):
    def __init__(self, name, optional=True):
        super().__init__(name, optional=optional)
        self.dict_body = DictionaryBody()


class Email(String):
    pass


class Password(String):
    pass


class ParamBuilder(object):
    def __init__(self, **kwargs):
        self.dict_body = DictionaryBody(**kwargs)

    def build(self, raw_param):
        result = {}
        self.root_dict.build(result, raw_param)
        return result