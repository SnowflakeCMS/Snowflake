# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/6/25


class Command(object):
    def __init__(self, seq, executor):
        self.seq = seq
        self.executor = executor
