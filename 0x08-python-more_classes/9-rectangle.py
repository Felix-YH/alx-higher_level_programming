#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize values
        Args:
            width = width of rectangle
            height = height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retuns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a rectangle
        Args:
        width
        height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of a rectangle
        Args:
            width
            height
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """print # in form of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ('')
        rec_gle = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_gle += str(self.print_symbol)
            rec_gle += '\n'
        return rec_gle[:-1]

    def __repr__(self):
        """return a string representation of the rectangle/
        to be able to recreate a new instance by using eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1 < rect_2:
            return rect_2
    @classmethod
    def square(cls, size=0):
        """that returns a new Rectangle/
         instance with width == height == size
         """
        return cls(size, size)
