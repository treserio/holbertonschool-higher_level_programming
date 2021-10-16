#!/usr/bin/python3
'''Write str to file and return number of chars written'''


def write_file(filename="", text=""):
    '''Write str to file and return number of chars written

    Args:
        filename: string for file to read in local dir
        text: string to write to file
    '''
    with open(filename, 'w', encoding='utf-8') as fd:
        return fd.write(text)
