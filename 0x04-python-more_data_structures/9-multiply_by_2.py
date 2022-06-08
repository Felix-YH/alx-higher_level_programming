#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    for key in sorted(new_d):
        print("{}: {}".format(key,new_d[key] * 2))
