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

    def to_json(self):
        '''Returns dictionary representation of obj'''
        return self.__dict__
