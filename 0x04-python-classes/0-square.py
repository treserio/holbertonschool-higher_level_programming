#!/usr/bin/python3
""" Don't be a square man ... or do! """


class Square:
    """ size initialized without type or value verification """

    def __init__(self, size):
        self.__size = size
