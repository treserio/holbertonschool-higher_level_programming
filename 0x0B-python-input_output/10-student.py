#!/usr/bin/python3
'''Module for Student class'''


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        '''Creates a Student

        Args:
            first_name: the student's first name
            last_name: the student's last name
            age: the student's age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns dictionary representation of obj'''
        if attrs != None:
            return {k: self.__dict__[k] for k in self.__dict__ if k in attrs}
        else:
            return self.__dict__
