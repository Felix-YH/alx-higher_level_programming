#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represent a square with public
    instance with getter and setter
    """

    def __init__(self, size=0):
        """Initialise a sqaure
        Args:
            size = size of square
        """
        self.__size = size

    @property
    def size(self):
        """Retrives size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current area"""
        return (self.__size ** 2)
