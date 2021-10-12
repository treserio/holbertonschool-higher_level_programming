#!/usr/bin/python3
'''Divides a matrix of numbers by a given value
'''


def matrix_divided(matrix, div):
    '''Confirms correct values and list structure before dividing matrix by
     div

    Args:
        matrix: a list of enenly sized lists
        div: a value to divide the matrix by
    Returns:
        a new matrix equal to the original divided by div
    '''
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    # check for uniform length of matrix with originLen & type of values in
    # lists
    originLen = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if originLen != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for val in row:
            if type(val) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    # check div for non-zero and int/float
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return[[round(val / div, 2) for val in row] for row in matrix]
