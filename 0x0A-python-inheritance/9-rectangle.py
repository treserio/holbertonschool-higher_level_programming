#!/usr/bin/python3
'''Validator version of Class BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class inheriting from '''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''return the str representation of the object'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        '''return area of rectangle w * h'''
        return self.__width * self.__height
