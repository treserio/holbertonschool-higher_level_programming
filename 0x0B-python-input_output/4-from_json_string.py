#!/usr/bin/python3
'''Return an object based on JSON string'''
import json


def from_json_string(my_str):
    '''Return an object based on JSON string

    Args:
        my_str: string to objectify
    '''
    return json.loads(my_str)
