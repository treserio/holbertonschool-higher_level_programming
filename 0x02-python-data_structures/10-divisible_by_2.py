#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        thing = []
        for x in my_list:
            thing.append(False if x%2 else True)
        return thing
