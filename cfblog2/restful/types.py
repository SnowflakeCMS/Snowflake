# -*- encoding: utf-8 -*-


class TypeBase(object):
    def __init__(self, optional=True):
        self._name = ""
        self._optional = optional

    def valid(self, parent):
        if not self._optional and self._name not in parent:
            return False
        else:
            return True


class Raw(TypeBase):
    def __init__(self, optional=True):


class Dict(TypeBase):
    pass

class String(TypeBase):
    """Normal text field
    """
    pass


class Email(String):
    pass


class Password(String):
    pass


class ParamValidator(object):
    pass
