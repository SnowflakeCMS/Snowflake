# -*- encoding: utf-8 -*-
# author:Shane Yao
# create@:2017/1/24
# Migration tools from other blog to cfblog2

import click

from cfblog2.tools.cfbm.migrate import *


@click.command("bm", short_help="Migrate other blog db to cfblog")
def run_command():
    from . import config
    fetcher = TypechoFetcher(config.fetcher)
    bm = BlogMigrate(fetcher)
    bm.start()
    bm.finish()
    bm.tear_down()
