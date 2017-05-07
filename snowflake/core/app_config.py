# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/3/13
import os


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

DefaultConfig = DevConfig

preset_config = {
    "dev": DevConfig,
    "product": ProductionConfig
}


def create_config(name, root_dir):
    conf = preset_config.get(name, DefaultConfig)()
    conf.SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(root_dir, "db.sqlite")
    return conf
