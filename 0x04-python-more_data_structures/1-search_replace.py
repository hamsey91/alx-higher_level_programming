#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == n_elem else n_elem for n_elem in my_list]
