#!/usr/bin/python3
'''Returns True if obj is of a_class or a subclass
'''


def is_kind_of_class(obj, a_class):
    '''Returns True if obj is of a_class or a subclass
    '''
    return(issubclass(type(obj), a_class))
