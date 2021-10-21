#!/usr/bin/python3
'''Base class for geometry classes'''


import json


class Base:
    '''Base class for geometry classes
    '''
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
    def save_to_file(cls, list_objs):
        '''Save list of class obj into <class>.json files'''
        with open(cls.__name__ + '.json', 'w') as fd:
            if list_objs:
                fd.write('[' + ', '.join(
                    cls.to_json_string(j.to_dictionary()) for j in list_objs) + ']')
            else:
                fd.write('[]')
        fd.close

    @classmethod
    def create(cls, **dictionary):
        return cls(**dictionary)

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json', 'r') as fd:
                return [cls.create(**j) for j in cls.from_json_string(fd.read())]
        except:
            return []

# -----------------
#   Static Methods
# -----------------
    @ staticmethod
    def from_json_string(json_string):
        if len(json_string) == 0:
            return []
        return json.loads(json_string)

    @ staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)
