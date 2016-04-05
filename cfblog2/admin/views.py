# -*- encoding: utf-8 -*-

from flask import render_template

from . import admin


@admin.route("/login")
def login():
    # TODO
    return "login"


@admin.route("/logout")
def logout():
    # TODO
    return "Logout"