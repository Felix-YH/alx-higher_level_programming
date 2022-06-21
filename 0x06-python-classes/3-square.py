#!/usr/bin/python3
"""Defines a square"""


class Square:
    """ Represent a square with public instance"""

    def __init__(self, size=0):
        """Initialise a sqaure
        Args:
            size = size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the current area"""
        return (self.__size ** 2)
