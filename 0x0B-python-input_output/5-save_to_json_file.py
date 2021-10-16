#!/usr/bin/python3
'''Write the JSON string of an obj to file'''
import json


def save_to_json_file(my_obj, filename):
    '''Write the JSON string of an obj to file'''
    with open(filename, 'w') as fd:
        return fd.write(json.dumps(my_obj))
