#!/usr/bin/python3
'''Returns true if obj is an instance of an inherited class'''


def inherits_from(obj, a_class):
    '''Returns true if obj is an instance of an inherited class
    '''
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
