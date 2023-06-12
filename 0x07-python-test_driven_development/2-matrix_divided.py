#!/usr/bin/python3
"""a function to scalar divde matrix"""


def matrix_divided(matrix, div):
    """divides matrix by scalar integer, rounded to two decimal places"""
    import decimal
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)

    row_len = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)

        row_len.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1

    if len(set(row_len)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))

    return new_matrix
