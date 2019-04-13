# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from nycrecords_flask.user.forms import ChangePasswordForm

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    """List members."""
    return render_template("users/members.html")


@blueprint.route("/profile")
@login_required
def profile():
    """Show the current users profile
    """
    form = ChangePasswordForm()
    return render_template("users/profile.html", form=form)


@blueprint.route("/change_password", methods=["POST"])
@login_required
def change_password():
    form = ChangePasswordForm(
        username=current_user.username,
        current_password=request.form.get("current_password", ""),
        new_password=request.form.get("new_passowrd", ""),
        confirm_new_password=request.form.get("confirm_new_passowrd", ""),
    )
    print(form.validate())
    return redirect(url_for("user.profile"))
