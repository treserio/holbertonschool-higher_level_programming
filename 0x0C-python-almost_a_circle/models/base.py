#!/usr/bin/python3
'''Base class for geometry classes'''


class Base:
    '''Base class for geometry classes
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Iniitialization Method'''
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
