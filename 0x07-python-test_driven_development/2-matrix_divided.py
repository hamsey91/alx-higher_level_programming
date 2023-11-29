#!/usr/bin/python3
"""Defines a moudule for matrix divided."""


def matrix_divided(matrix, div):
    """Function to divide elements of matrix by divisor.
    Args:
        matrix: list of lists of numbers
        div: the divisor number
    Returns:
        list: list of lists representing divided matrix.
    Raises:
        TypeError: matrix is not list of lists of numbers.
        TypeError: lists are not all same number of row.
        TypeError: divisor is not numbers.
        ZeroDivisionError: divisor is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for a in row:
            if not isinstance(a, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(a / div, 2) for a in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
