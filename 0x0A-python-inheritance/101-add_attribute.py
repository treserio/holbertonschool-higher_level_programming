#!/usr/bin/python3
'''Add attribute to obj if able'''


def add_attribute(obj, key, val):
    '''Add attribute to obj if able'''
    if hasattr(obj, '__dict__'):
        setattr(obj, key, val)
    else:
        raise TypeError("can't add new attribute")
