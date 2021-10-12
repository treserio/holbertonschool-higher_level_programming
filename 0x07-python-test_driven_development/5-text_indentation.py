#!/usr/bin/python3
'''Print input str with 2 \\n\\n after . ? and :
'''


def text_indentation(text):
    '''Print input str with 2 \\n\\n after . ? and :
    '''
    print(text.replace(". ", ".\n\n").replace("? ", "?\n\n")
          .replace(": ", ":\n\n"), end="")
