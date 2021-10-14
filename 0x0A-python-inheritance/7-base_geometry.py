#!/usr/bin/python3
'''Validator version of Class BaseGeometry'''


class BaseGeometry:
    '''BaseGeometry class, unknown purpose, method area raises exception'''

    def area(self):
        '''Raise exception area() is not implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
