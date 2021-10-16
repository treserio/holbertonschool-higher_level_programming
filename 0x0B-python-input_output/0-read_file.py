#!/usr/bin/python3
'''Read a file and print to stdout'''


def read_file(filename=""):
    '''Read a file and print to stdout

    Args:
        filename: string for file to read in local dir
    '''
    with open(filename, 'r') as fd:
        print(fd.read(), end="")
