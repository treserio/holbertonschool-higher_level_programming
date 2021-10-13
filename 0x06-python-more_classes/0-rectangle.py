#!/usr/bin/python3
'''Module for Setting up a Rectangle class
'''


class Rectangle:
    '''Rectangle object

    Attributes
    ----------
    width: int
        must be >= 0
    height: int
        must be >= 0
    '''

    def __init__(self, width=0, height=0):
        '''Init method with defaults of 0 for width and height
        also confirms values are ints and >= 0
        '''
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        '''return width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''return height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
