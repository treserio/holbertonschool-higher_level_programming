#!/usr/bin/python3
'''This module fetches a URL with urllib'''


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        print('Body response:')
        print('\t- type: {}'.format(type(r.read())))
        print('\t- content: {}'.format(r.read()))
        print('\t- utf8 content: {}'.format(r.read().decode('UTF-8')))
