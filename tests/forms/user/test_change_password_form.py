# -*- coding: utf-8 -*-
"""Test the New User Registration form."""

from nycrecords_flask.user.forms import ChangePasswordForm


def test_validate_success(user):
    """Change password successful."""
    user.set_password("example")
    user.save()
    form = ChangePasswordForm(
        username=user.username,
        current_password="example",
        new_password="Password",
        confirm_new_password="Password",
    )
    assert form.validate() is True


def test_validate_incorrect_current_password(user):
    """Current password does not match."""
    user.set_password("example")
    user.save()
    form = ChangePasswordForm(
        username=user.username,
        current_password="password",
        new_password="Password",
        confirm_new_password="Password",
    )
    assert form.validate() is False
    assert "Current password does not match." in form.current_password.errors


def test_validate_incorrect_confirm_password(user):
    """New Password and New Password Confirmation do not match."""
    user.set_password("example")
    user.save()
    form = ChangePasswordForm(
        username=user.username,
        current_password="example",
        new_password="example",
        confirm_new_password="example",
    )
    assert form.validate() is False
    assert (
        "Current Password and New Password must not match." in form.new_password.errors
    )


def test_validate_missing_current_password(user):
    """Missing current_password."""
    user.set_password("example")
    user.save()
    form = ChangePasswordForm(
        username=user.username,
        new_password="example",
        confirm_new_password="example",
    )
    assert form.validate() is False
    assert (
        "This field is required." in form.current_password.errors
    )


def test_validate_missing_new_password(user):
    """Missing new_password."""
    user.set_password("example")
    user.save()
    form = ChangePasswordForm(
        username=user.username,
        current_password="example",
        confirm_new_password="password",
    )
    assert form.validate() is False
    assert (
        "This field is required." in form.new_password.errors
    )


def test_validate_missing_confirm_new_password(user):
    """Missing confirm_new_password."""
    user.set_password("example")
    user.save()
    form = ChangePasswordForm(
        username=user.username,
        current_password="example",
        new_password="password",
    )
    assert form.validate() is False
    assert (
        "This field is required." in form.confirm_new_password.errors
    )