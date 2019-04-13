# -*- coding: utf-8 -*-
"""Test Login Functionality."""


def test_about_page_content(testapp):
    """Test content of About page"""
    res = testapp.get("/about").follow()
    print(res)
    assert "About" in res
