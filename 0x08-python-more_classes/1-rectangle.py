#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize values
        Args:
            width = width of rectangle
            height = height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retuns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width to value"""
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be integer")
        self.__width = value

    @property
    def height(self):
        """returns width of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set width to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be integer")
        self.__height = value


