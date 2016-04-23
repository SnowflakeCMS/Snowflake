# -*- encoding: utf-8 -*-

from flask import render_template, redirect, url_for
from flask import request, current_app, g, session, flash
from flask.views import View

from . import admin
from .forms import LoginForm
from .models import User

LOGIN_STATUS_NONE = 0
LOGIN_STATUS_SUCCESS = 1
LOGIN_STATUS_FAILED = 2


# Login checker
def login_required(controller):
    def __controller_with_login_check(*args, **kwargs):
        login_status = session.get("login_status", LOGIN_STATUS_NONE)
        if login_status != LOGIN_STATUS_SUCCESS:
            return redirect(url_for("admin.login"))
        else:
            return controller(*args, **kwargs)

    __controller_with_login_check.__name__ = controller.__name__
    return __controller_with_login_check


@admin.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        # current_app
        fv_username = form.username.data
        fv_password = form.password.data
        current_app.logger.debug("Form.UserName:%s, password:%s", fv_username, fv_password)
        user = User.query.filter_by(username=fv_username, password=fv_password).first()
        if user is None:
            # Login Failed
            # TODO i18n
            flash("login failed")
        else:
            session["login_status"] = LOGIN_STATUS_SUCCESS
            session["login_user_id"] = user.id
        return redirect(url_for(".index"))
    else:
        return render_template("admin_login.html", form=form)


@admin.route("/logout")
def logout():
    session.pop("login_status")
    session.pop("login_user_id")
    return "Logout"


@admin.route("/")
def index():
    return redirect(url_for("admin.dashboard"))


@admin.route("/dashboard")
@login_required
def dashboard():
    return "This is a dashboard"


@admin.route("/blog/new")
def blog_new():
    pass
