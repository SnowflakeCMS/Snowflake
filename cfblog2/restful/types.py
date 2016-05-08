# -*- encoding: utf-8 -*-


class TypeBase(object):
    def __init__(self):
        self._name = ""


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



