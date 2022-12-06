#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in my_list:
        length_of_num = len(my_list)
        for numbers in range(length, -1):
            print("{:d}".format(my_list(numbers)))
