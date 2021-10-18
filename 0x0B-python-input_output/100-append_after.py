#!/usr/bin/python3
'''Insert text after line containing certain strings'''


def append_after(filename="", search_string="", new_string=""):
    '''Insert text after line containing certain strings

    Args:
        filename: the file to insert text in
        search_string: the text to insert a new line after
        new_string: the line to insert into the file
    '''
    with open(filename, 'r') as fd:
        fd_text = ""
        for ln in fd:
            fd_text += ln
            if search_string in ln:
                fd_text += new_string

    with open(filename, 'w') as fd:
        fd.write(fd_text)
