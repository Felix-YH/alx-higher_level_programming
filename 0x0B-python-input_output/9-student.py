#!/usr/bin/python3
"""This write a class Student that defines a student"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """"Retrieves a dictionary representation of a
        Student instance.Returns:the dict representation
        of the instance
        """
        return self.__dict__
