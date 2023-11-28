#!usr/bin/python3
"""defines a  function that prints a text"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'.

    Args:
        text: the size length of the square.

    Raises:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for d in ".?:":
        text = (d + "\n\n").join(
            [line.strip(" ") for line in text.split(d)])

    print(text, end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")
