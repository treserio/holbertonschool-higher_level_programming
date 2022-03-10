#!/usr/bin/python3
'''This module posts an email with requests.'''


if __name__ == '__main__':
    import requests
    import sys

    req = requests.post(sys.argv[1], {'email': sys.argv[2]})

    print(req.text)
