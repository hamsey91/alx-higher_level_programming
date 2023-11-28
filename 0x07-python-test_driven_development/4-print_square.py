#!usr/bin/python3
"""defines a function that prints a square"""


def print_square(size):
    """Print a square with the character '#'.

    Args:
        size: the size length of the square.

    Raises:
        TypeError: the size must be an integer.
        ValueError: the size must be greater or equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/4-print_square.txt")
