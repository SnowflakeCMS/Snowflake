# -*- encoding: utf-8 -*-
# author:Shane Yao
# create@:2017/1/24
# Migration tools from other blog to snowflake

import click

from snowflake.tools.cfbm.migrate import *


@click.command("bm", short_help="Migrate other blog db to cfblog")
def run_command():
    from flask import current_app
    migrate_config = current_app.snowflake_config["TOOLS_MIGRATE"]
    print(migrate_config)
    fetcher = TypechoFetcher(migrate_config["FETCHER"])
    bm = BlogMigrate(fetcher)
    bm.start()
    bm.finish()
    bm.tear_down()
