#!/usr/bin/python3
"""This module returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly
    an instance,otherwise False
    Args:
        obj:object to verfiy
        a_class:class to check the instance
    """
    if type(obj) is a_class:
        return True
    else:
        return False
