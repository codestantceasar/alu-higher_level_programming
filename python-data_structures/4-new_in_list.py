#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying
    the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element.
        element: The new element to insert.

    Returns:
        list: A new list with the element replaced if idx is valid,
              otherwise a copy of the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
