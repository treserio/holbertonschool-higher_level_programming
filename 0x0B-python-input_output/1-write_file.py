#!/usr/bin/python3
'''Write str to file and return number of chars written'''


def write_file(filename="", text=""):
    '''Write str to file and return number of chars written'''
    with open(filename, 'w', encoding='utf-8') as fd:
        return fd.write(text)
