#!/usr/bin/python3
def matrix_divided(matrix, div):
    for row in matrix:
        for col in row:
            if (not isinstance(col, int) and not isinstance(col, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for roww in matrix:
        if not(len(roww) == len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[round(i / div, 2) for i in roww] for roww in matrix]
    return (new_mat)
