#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    end_space = ' '
                else:
                    end_space = ''
                print("{:d}".format(matrix[row][item]), end=end_space)
            print()
