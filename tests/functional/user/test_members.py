# -*- coding: utf-8 -*-
"""Test members functionality."""
from tests.helpers.authentication import login


def test_members_endpoint(testapp, user):
    """GET /users/"""
    res = login(testapp, user)
    res = testapp.get("/users/")
    assert "Welcome {username}".format(username=user.username) in res


def test_member_profile(testapp, user):
    """GET /users/"""
    res = login(testapp, user)
    res = testapp.get("/users/profile")
    assert "Profile: {username}".format(username=user.username) in res
