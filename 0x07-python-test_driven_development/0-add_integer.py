#!/usr/bin/env python3
'''Adds 2 ints or floats(cast as ints)
'''


def add_integer(a, b=98):
    '''Adds 2 ints or floats and returns them as int

    Args:
        a: first value to add
        b: second value to add
    Returns:
        int(a + b)
    '''
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
