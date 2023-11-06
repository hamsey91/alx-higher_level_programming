#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list = []
    if my_list:
        for num in my_list:
            div_list.append(False if num % 2 else True)
        return div_list
