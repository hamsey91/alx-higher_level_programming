#!/usr/bin/python3
def remove_char_at(str, i):
    if i < 0:
        return str
    return str[0:i] + str[i+1:]
