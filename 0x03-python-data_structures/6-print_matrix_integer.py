#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        space = ""
        for item in array:
            print("{}{:d}".format(space, item), end="")
            space = " "
        print()
