#!/usr/bin/python3
'''base init method'''


def __init__(self, id=None):
    self.__nb_objects = 0
    if id != None:
        self.id = id
    else:
        self.__nb_objects += 1
        self.id = self.__nb_objects
