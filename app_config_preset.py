# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/3/13


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "db.sqlite")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.debug = True


class DevConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False


preset_config = {
    "dev": DevConfig,
    "product": ProductionConfig
}

def get_preset(name):
    return preset_config.get(name)
