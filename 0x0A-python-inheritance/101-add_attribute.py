#!/usr/bin/python3
def add_attribute(obj, key, val):
    if hasattr(obj, '__dict__'):
        setattr(obj, key, val)
    else:
        raise TypeError("can't add new attribute")
