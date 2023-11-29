#!/usr/bin/python3
"""Defines a module for matrix_mul."""


def matrix_mul(m_a, m_b):
    """Function to multiplies one matrix by another.
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the product of the 2 matrix.
    Raises:
        TypeError: m_a or m_b are not lists.
        TypeError: m_a or m_b are not lists of lists.
        ValueError: m_a or m_b are empty lists.
        TypeError: m_a or m_b contain a non numbers.
        TypeError: m_a or m_b row not the same size.
        ValueError: m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_empty = False
    m_b_empty = False
    m_a_not_r = False
    m_b_not_r = False
    m_a_not_n = False
    m_b_not_n = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_not_r = True
        for n in row:
            if not isinstance(n, (int, float)):
                m_a_not_n = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_not_r = True
        for n in row:
            if not isinstance(n, (int, float)):
                m_b_not_n = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_not_n:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_not_n:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_not_r:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_not_r:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            product[i].append(s)

    return product

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
