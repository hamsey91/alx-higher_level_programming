#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is type(roman_string) != str or None:
        return 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [digits[a] for a in roman_string] + [0]
    total = 0

    for i in range(len(num) - 1):
        if num[i] >= num[i+1]:
            total += num[i]
        else:
            total -= num[i]

    return total
