# -*- coding: utf-8 -*-
"""Authentication helpers for pytest.

This module contains helper functions dealing with authentication.
"""


def login(testapp, user):
    """Logs a user in to the test app.
    
    Args:
        testapp ([type]): [description]
        user ([type]): [description]
    """
    res = testapp.get("/")

    # Fills out login form in navbar
    form = res.forms["loginForm"]
    form["username"] = user.username
    form["password"] = "myprecious"

    # Submits
    return form.submit().follow()
