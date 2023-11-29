#!/usr/bin/python3
"""Defines module for text_indentation."""


def text_indentation(text):
    """Functcion to addi 2 newlines after '.?:' chars.

    Args:
        text: The text string.

    Raises:
        TypeError: text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiters in ".?:":
        text = (delimiters + "\n\n").join(
            [line.strip(" ") for line in text.split(delimiters)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
