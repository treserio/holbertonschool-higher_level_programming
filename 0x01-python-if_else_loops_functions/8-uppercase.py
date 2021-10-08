#!/usr/bin/python3
def uppercase(str):
    print("".join(chr(ord(l)-32) if l >= 'a' and l <= 'z' else l for l in str))
