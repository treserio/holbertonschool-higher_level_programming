#!/usr/bin/python3
'''Return the JSON of an obj'''
import json


def to_json_string(my_obj):
    '''Return the JSON of an obj

    Args:
        my_obj: object to JSONify
    '''
    return json.dumps(my_obj)
