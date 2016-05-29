# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for
from . import admin


@admin.route("/")
def index():
    return redirect(url_for)
