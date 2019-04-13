# -*- coding: utf-8 -*-
"""Test the New User Registration form."""

from nycrecords_flask.user.forms import RegisterForm


def test_validate_user_already_registered(user):
    """Enter username that is already registered."""
    form = RegisterForm(
        username=user.username,
        email="foo@bar.com",
        password="example",
        confirm="example",
    )

    assert form.validate() is False
    assert "Username already registered" in form.username.errors


def test_validate_email_already_registered(user):
    """Enter email that is already registered."""
    form = RegisterForm(
        username="unique", email=user.email, password="example", confirm="example"
    )

    assert form.validate() is False
    assert "Email already registered" in form.email.errors


def test_validate_success(db):
    """Register with success."""
    form = RegisterForm(
        username="newusername",
        email="new@test.test",
        password="example",
        confirm="example",
    )
    assert form.validate() is True
