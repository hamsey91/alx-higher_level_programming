#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} argument(s):".format(num_args))
    for index in range (num_args):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
