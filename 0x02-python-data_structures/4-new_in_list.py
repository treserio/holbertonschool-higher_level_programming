#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < len(my_list) and idx >= 0:
        thing = my_list[:]
        thing[idx] = element
        return thing
    else:
        return my_list
