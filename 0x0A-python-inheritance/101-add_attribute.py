#!/usr/bin/python3
def add_attribute(obj, key, val):
    if type(obj) not in [int, float, tuple, str, list, dict]:
        if not hasattr(obj, key):
            setattr(obj, key, val)
    else:
        raise TypeError("can't add new attribute")
