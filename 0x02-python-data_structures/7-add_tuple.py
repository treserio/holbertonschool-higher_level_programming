#!/usr/bin/python3
from itertools import zip_longest
def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(sum(x) for x in zip_longest(tuple_a, tuple_b, fillvalue=0))
