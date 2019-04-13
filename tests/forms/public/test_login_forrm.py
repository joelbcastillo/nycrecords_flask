# -*- coding: utf-8 -*-
"""Test the New User Registration form."""

from nycrecords_flask.public.forms import LoginForm


def test_validate_success(user):
    """Login successful."""
    user.set_password("example")
    user.save()
    form = LoginForm(username=user.username, password="example")
    assert form.validate() is True
    assert form.user == user


def test_validate_missing_username(db):
    """Missing username."""
    form = LoginForm(password="password")
    assert form.validate() is False
    print(form.username.errors)
    assert "This field is required." in form.username.errors
    assert form.user is None


def test_validate_missing_password(db):
    """Missing username."""
    form = LoginForm(username="username")
    assert form.validate() is False
    print(form.password.errors)
    assert "This field is required." in form.password.errors
    assert form.user is None


def test_validate_unknown_username(db):
    """Unknown username."""
    form = LoginForm(username="unknown", password="example")
    assert form.validate() is False
    assert "Unknown username" in form.username.errors
    assert form.user is None


def test_validate_invalid_password(user):
    """Invalid password."""
    user.set_password("example")
    user.save()
    form = LoginForm(username=user.username, password="wrongpassword")
    assert form.validate() is False
    assert "Invalid password" in form.password.errors


def test_validate_inactive_user(user):
    """Inactive user."""
    user.active = False
    user.set_password("example")
    user.save()
    # Correct username and password, but user is not activated
    form = LoginForm(username=user.username, password="example")
    assert form.validate() is False
    assert "User not activated" in form.username.errors
