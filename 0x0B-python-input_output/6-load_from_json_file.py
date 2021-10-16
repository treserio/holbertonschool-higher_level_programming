#!/usr/bin/python3
'''Return an object based on JSON from file'''
import json


def load_from_json_file(filename):
    '''Return an object based on JSON from file

    Args:
        filename: file to read JSON from
    '''
    with open(filename, 'r') as fd:
        return json.loads(fd.read())
