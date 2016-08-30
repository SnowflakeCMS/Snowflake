# -*- encoding: utf-8 -*-
from flask import current_app


def log_info(*args, **kwargs):
    current_app.logger.info(*args, **kwargs)


def log_debug(*args, **kwargs):
    current_app.logger.debug(*args, **kwargs)


def log_warn(*args, **kwargs):
    current_app.logger.warn(*args, **kwargs)


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)

