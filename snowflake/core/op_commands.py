# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/5/12


class OpCommand(object):
    def __init__(self, seq, executor):
        self.seq = seq
        self.executor = executor


class OpCommandFactory(object):

    def create_command(self, name, seq, *args, **kwargs):
        pass