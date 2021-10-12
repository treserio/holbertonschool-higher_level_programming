#!/usr/bin/python3
"""Module to return the max value of a list
"""


def max_integer(list=[]):
    '''Return the max value from a numeric list
    '''
    if list:
        return sorted(list)[-1]
