#!/usr/bin/python3
'''Creates a model of Pascal's Triangle as a list of lists'''


def pascal_triangle(n):
    '''Creates a model of Pascal's Triangle as a list of lists'''
    tri = []
    for r in range(n):
        row = []
        for val in range(r + 1):
            if val == 0 or val == r:
                row.append(1)
            else:
                row.append(tri[r - 1][val - 1] + tri[r - 1][val])
        tri.append(row)

    return tri
