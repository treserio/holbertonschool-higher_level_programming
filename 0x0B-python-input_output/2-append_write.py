#!/usr/bin/python3
'''Append str to file and return number of chars written'''


def append_write(filename="", text=""):
    '''Append str to file and return number of chars written

    Args:
        filename: string for file to read in local dir
        text: string to write to file
    '''
    with open(filename, 'a', encoding='utf-8') as fd:
        return fd.write(text)
