# -*- encoding: utf-8 -*-
# author:Shane Yao
# create@:2017/1/28
# Setup scripts for deploy

from setuptools import setup

setup(
    name='snowflake',
    version='0.1',
    long_description=__doc__,
    packages=['snowflake'],
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask", "flask-sqlalchemy", "flask-migrate", "PyMySQL", "CommonMark"]
)
