#!usr/bin/python3
"""defines a function that divides matrix."""


def matrix_divided(matrix, div):
    """division of all elements of matrix.

    Args:
        matrix : list of lists of integers or floats.
        div: the divisor.

    Raises:
        TypeError: matrix must be a list of lists of integers or floats.
        TypeError: Each row of the matrix must be of the same size.
        TypeError: div must be a number (integer or float).
        ZeroDivisionError: div can’t be equal to 0.
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of '
                        'integers/floats')
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of '
                            'integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for a in row:
            if not isinstance(a, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')
    return [[round(a / div, 2) for a in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
