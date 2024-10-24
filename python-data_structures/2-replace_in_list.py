#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specified index.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace the element.
        element (int): The new element to insert at the specified index.

    Returns:
        list: The modified list if index is valid, else the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
