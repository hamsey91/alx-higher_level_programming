#!usr/bin/python3
"""defines a function that prints full name"""


def say_my_name(first_name, last_name=""):
    """Print first & last name.

    Args:
        first_name: First name to be printed.
        last_name: last name to be printed.

    Raises:
        TypeError: first_name and last_name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/3-say_my_name.txt")
