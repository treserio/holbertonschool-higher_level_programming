#!/usr/bin/python3
'''This module displays the value of X-Request-ID'''


if __name__ == '__main__':
    import sys
    import urllib.parse
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as r:
        print('{}'.format(r.info().get('X-Request-ID')))
