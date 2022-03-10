#!/usr/bin/python3
'''This module posts an email with Python'''


if __name__ == '__main__':
    import sys
    from urllib import request, parse

    data = parse.urlencode({'email': sys.argv[2]})
    req = request.Request(sys.argv[1], data.encode('UTF-8'))

    with request.urlopen(req) as r:
        print(r.read().decode('UTF-8'))
