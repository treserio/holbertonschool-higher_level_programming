#!/usr/bin/python3
'''This module handles errors for requests'''


if __name__ == '__main__':
    import requests
    import sys

    req = requests.get(sys.argv[1])

    stc = req.status_code

    if stc >= 400:
        print('Error code: {}'.format(stc))

    else:
        print(req.text)
