#!/usr/bin/python3
'''Write str to file and return number of chars written'''


def write_file(filename="", text=""):
    with open(filename, 'w') as fd:
        return fd.write(text)
