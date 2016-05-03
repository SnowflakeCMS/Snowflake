# -*- encoding: utf-8 -*-


class ParamBase(object):
    def __init__(self):
        self._name = ""


class Text(ParamBase):
    """Normal text field
    """
    pass


class Email(Text):
    pass


class Password(Text):
    pass



