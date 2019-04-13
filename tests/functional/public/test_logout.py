# -*- coding: utf-8 -*-
"""Test Logout endpoint."""
from flask import url_for

from tests.helpers.authentication import login


def test_logout_endpoint(user, testapp):
    res = login(testapp, user)
    res = testapp.get(url_for("public.logout")).follow()
    assert "You are logged out" in res
