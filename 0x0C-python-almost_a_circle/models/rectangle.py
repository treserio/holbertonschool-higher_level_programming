#!/usr/bin/python3
'''Rectangle class inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherits from Base'''

    def verify_WH(self, nm, val):
        if type(val) is not int:
            raise TypeError("{} must be an integer".format(nm))
        if val <= 0:
            raise ValueError("{} must be > 0".format(nm))

    def verify_XY(self, nm, val):
        if type(val) is not int:
            raise TypeError("{} must be an integer".format(nm))
        if val < 0:
            raise ValueError("{} must be >= 0".format(nm))

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.verify_WH("width", width)
        self.__width = width
        self.verify_WH("height", height)
        self.__height = height
        self.verify_XY("x", x)
        self.__x = x
        self.verify_XY("y", y)
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.verify_WH("width", val)
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.verify_WH("height", val)
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.verify_XY("x", val)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.verify_XY("y", val)
        self.__y = val

    def area(self):
        return self.width * self.height

    def display(self):
        if self.y:
            print("\n"*(self.y - 1))
        print("\n".join(" "*self.x+"#"*self.width for i in range(self.height)))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        attr = ('id', 'width', 'height', 'x', 'y')
        for i in range(len(args)):
            setattr(self, attr[i], args[i])
