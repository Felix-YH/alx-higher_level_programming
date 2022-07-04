#!/usr/bin/python3
"""This module eturns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """Return the available attributes"""
    return dir(obj)
