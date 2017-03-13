# -*- encoding: utf-8 -*-
from flask import current_app


def log_info(*args, **kwargs):
    return current_app.logger.info(*args, **kwargs)


def log_debug(*args, **kwargs):
    return current_app.logger.debug(*args, **kwargs)


def log_warn(*args, **kwargs):
    return current_app.logger.warn(*args, **kwargs)


def log_error(*args, **kwargs):
    return current_app.logger.error(*args, **kwargs)

