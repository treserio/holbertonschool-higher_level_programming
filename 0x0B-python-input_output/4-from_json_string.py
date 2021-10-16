#!/usr/bin/python3
'''Return an object based on JSON string'''
import json


def to_json_string(my_obj):
    '''Return an object based on JSON string'''
    return json.loads(my_obj)
