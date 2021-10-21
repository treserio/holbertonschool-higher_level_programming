#!/usr/bin/python3
'''Square class inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''init method for square'''
        self.verify_WH("size", size)
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of object'''
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size getter'''
        return self.width

    @size.setter
    def size(self, val):
        '''Size setter with validation, using inherited width & height'''
        self.width = self.verify_WH("width", val)
        self.height = self.verify_WH("height", val)

    def update(self, *args, **kwargs):
        '''Updates attributes in specific order for args, and with key:val pairs for kwargs'''
        attr = ('id', 'size', 'x', 'y')
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''String version of JSON interpretation'''
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
