# -*- encoding: utf-8 -*-

from flask import render_template
from flask import request, current_app, g, session, flash

from . import admin, forms
from .forms import LoginForm
from .models import User


@admin.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        flash("Complete")
        # current_app
        User.query.filter_by(username=form.username, password=form.password)
        return render_template("admin_login.html", form=form)
    else:
        return render_template("admin_login.html", form=form)


@admin.route("/logout")
def logout():
    # TODO
    return "Logout"