# -*- encoding: utf-8 -*-
# author:Shane Yao
# create@:2017/1/24

from .click_main import run_command


def init(app):
    app.app_context().push()
    app.cli.add_command(run_command)
