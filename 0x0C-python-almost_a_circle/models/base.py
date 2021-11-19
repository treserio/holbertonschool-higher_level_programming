#!/usr/bin/python3
'''Base class for geometry classes'''


import json
import csv
import turtle


class Base:
    '''Base class for geometry classes'''
#   object counter
    __nb_objects = 0

# --------------
#   Init Method
# --------------
    def __init__(self, id=None):
        '''Iniitialization Method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# --------------------
#   Input Verification
# --------------------
    def verify_WH(self, nm, val):
        '''Value verification for width & height'''
        if type(val) is not int:
            raise TypeError("{} must be an integer".format(nm))
        if val <= 0:
            raise ValueError("{} must be > 0".format(nm))
        return val

    def verify_XY(self, nm, val):
        '''Value verification for x & y'''
        if type(val) is not int:
            raise TypeError("{} must be an integer".format(nm))
        if val < 0:
            raise ValueError("{} must be >= 0".format(nm))
        return val

# ----------------
#   Class Methods
# ----------------
    @classmethod
    def create(cls, **dictionary):
        '''instantiate a cls obj based on kwargs(**dictionary)'''
        # return cls(**dictionary)
        dum = cls(**dictionary)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        '''Return a list ot instantiated objects'''
        try:
            with open(cls.__name__ + '.json', 'r') as fd:
                return [cls.create(**j)
                        for j in cls.from_json_string(fd.read())]
        except:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save list of class obj into <class>.json files'''
        with open(cls.__name__ + '.json', 'w') as fd:
            if list_objs:
                fd.write('[' + ', '.join(
                    cls.to_json_string(j.to_dictionary())
                    for j in list_objs) + ']')
            else:
                fd.write('[]')

    @classmethod
    def load_from_file_csv(cls):
        '''load geometric objects from associated csv files'''
        if cls.__name__ == 'Rectangle':
            fields = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            fields = ['id', 'size', 'x', 'y']
        with open(cls.__name__ + '.csv', 'r') as fd:
            data = list(csv.reader(fd))
            crt_lst = []
            for l in data:
                crt_lst.append({fields[i]: int(l[i])
                               for i in range(len(fields))})

        return [cls.create(**d) for d in crt_lst]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save geometric objects to associated csv files'''
        if cls.__name__ == 'Rectangle':
            fields = ['id', '_Rectangle__width', '_Rectangle__height',
                      '_Rectangle__x', '_Rectangle__y']
        elif cls.__name__ == 'Square':
            fields = ['id', '_Rectangle__width',
                      '_Rectangle__x', '_Rectangle__y']
        with open(cls.__name__ + '.csv', 'w') as fd:
            wr_str = ""
            for ob in list_objs:
                wr_str += ",".join(str(vars(ob)[key]) for key in fields)
                wr_str += '\n'
            fd.write(wr_str)

# -----------------
#   Static Methods
# -----------------
    @ staticmethod
    def from_json_string(json_string):
        '''Return a list of dictionary obj based on JSON string'''
        if json_string and len(json_string) > 0:
            return json.loads(json_string)
        return []

    @ staticmethod
    def to_json_string(list_dictionaries):
        '''Return JSON string representation of list of dict'''
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return '[]'

    @staticmethod
    def draw(rec_list, sq_list):
        '''using turtle module to draw shapes'''
        for rec in rec_list:
            turtle.penup()
            turtle.setpos(rec.x, rec.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rec.height)
                turtle.right(90)
                turtle.forward(rec.width)
                turtle.right(90)
            turtle.clearscreen()
        for sq in sq_list:
            turtle.penup()
            turtle.setpos(sq.x, sq.y)
            turtle.pendown()
            for i in range(4):
                turtle.forward(sq.size)
                turtle.right(90)
            turtle.clearscreen()
