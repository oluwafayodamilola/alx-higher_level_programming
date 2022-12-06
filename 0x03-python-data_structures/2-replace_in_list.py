#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
        Replace an element from a list

        Args:
            my_list: list to replace from
            idx: index to replace element
            element: item to be replaced with
        Return:
            my_list
    """
    if idx < 0:
        return(my_list)
    if idx >= my_list:
        return(my_list)
    for index in range(len(my_list)):
        if index == idx:
            mylist[index] = element
            return my_list
