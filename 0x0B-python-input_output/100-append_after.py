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
        fd_text = fd.readlines()

    for ln in range(len(fd_text)):
        if search_string in fd_text[ln]:
            fd_text.insert(ln + 1, new_string)

    with open(filename, 'w') as fd:
        fd_text = "".join(fd_text)
        fd.write(fd_text)
