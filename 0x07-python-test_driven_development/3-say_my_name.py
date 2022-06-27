#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Function the print first and last names
    Args:
    first_name = First name of person
    last_name = Last name of the person
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
