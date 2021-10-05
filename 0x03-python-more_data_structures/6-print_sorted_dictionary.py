#!/usr/bin/python3
def print_sorted_dictionary(a_dic):
    print("\n".join("{}: {}".format(x, a_dic[x]) for x in sorted(a_dic)))
