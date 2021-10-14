#!/usr/bin/python3
'''Validator version of Class BaseGeometry'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Rectangle class inheriting from'''

    def __init__(self, size):
        '''Square init method that also sets height and width'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
