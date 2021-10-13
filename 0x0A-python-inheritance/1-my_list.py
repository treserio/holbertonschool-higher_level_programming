#!/usr/bin/python3
'''prints the sorted list'''


class MyList(list):
    '''inherits from list and prints the sorted list
    '''

    def print_sorted(self):
        print(sorted(self))
