#!/usr/bin/python3
"""This module returns the addtion of two integers"""


def add_integer(a, b=98):
    """Function that adds two integers

    Args:
    a = first integer
    b= secong integer = 98

    raise a TypeError when a or b is not an integer

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be integer")
    return (int(a) + int(b))
