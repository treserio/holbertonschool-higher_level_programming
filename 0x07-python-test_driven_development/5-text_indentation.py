#!/usr/bin/python3
'''Print input str with 2 \\n\\n after . ? and :
'''


def text_indentation(text):
    '''Print input str with 2 \\n\\n after . ? and :
    '''
    if type(text) == str:
        text = text.replace(".", ".~~").replace("?", "?~~").replace(":", ":~~")
        print("\n\n".join(i.strip() for i in text.split('~~')), end="")
    else:
        raise TypeError("text must be a string")
