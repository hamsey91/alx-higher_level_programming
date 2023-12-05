#!/usr/bin/python3
"""Script that adds all arguments to a list and save them to a file."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =__import__('6-load_from_json_file').load_from_json_file


try:
    Data = load_from_json_file("add_item.json")
except FileNotFoundError:
    Data = []
Data.extend(sys.argv[1:])
save_to_json_file(Data, "add_item.json")
