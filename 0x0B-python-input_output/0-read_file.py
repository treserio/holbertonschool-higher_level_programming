#!/usr/bin/python3
'''Read a file and print to stdout'''


def read_file(filename=""):
    '''Read a file and print to stdout'''
    with open(filename, 'r') as fd:
        print(fd.read(), end="")