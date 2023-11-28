#!usr/bin/python3
"""defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """Addition of 2 integers.

    Args:
        a: First number.
        b: Second number.

    Raises:
        TypeError: a and b must be integers or floats.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__=="__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
