# -*- encoding: utf-8 -*-
# author:Shane Yao(future0906@gmail.com)
# create@:2017/3/13

SECRET_KEY = "dummy_key"

SNOWFLAKE_PRESET = "dev"
SNOWFLAKE_KEY = SECRET_KEY

SNOWFLAKE_TOOLS_MIGRATE = {
    "FETCHER": {
        "host": "localhost",
        "user": "dummy_user",
        "password": "dummy_password",
        "db": "db",
        "charset": "utf8",
        "port": 3306,
    }
}
