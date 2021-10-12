#!/usr/bin/python3
'''Prints a square of size dimensions
'''


def print_square(size):
    '''Prints a square of size dimensions

    Args:
        size: dimensions of the square to print
    '''
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if size:
        print("\n".join(("#"*size) for x in range(size)))
