#!/usr/bin/python3
def print_sorted_dictionary(dic):
    print("\n".join("{}: {}".format(x, dic[x]) for x in sorted(dic) if dic))
