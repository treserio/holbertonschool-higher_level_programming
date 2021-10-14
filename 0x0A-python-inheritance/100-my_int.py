#!/usr/bin/python3
'''Inverse eq and neq functions for class
'''


class MyInt(int):
    '''Inverse eq and neq functions for class
    '''

    def __init__(self, val):
        self.val = val

    def __eq__(self, obj):
        return self.val != obj

    def __ne__(self, obj):
        return self.val == obj
