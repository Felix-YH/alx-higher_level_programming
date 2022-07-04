#!/usr/bin/python3
"""This module write a class MyList that inherits from list"""


class MyList(list):
    """MyList inherits list"""
    def print_sorted(self):
        """Return the list of sorted integers"""
        st_list = self[:]
        st_list.sort()
        print("{}".format(st_list))
