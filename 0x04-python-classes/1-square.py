#!/usr/bin/python3
""" Don't be a square man ... or do! """


class Square:
    """ size with type or value verification """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
