#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list at a specified index.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        int or None: The element at the specified index, or None if index is
                   invalid.
    """
    if not isinstance(idx, int):
        return None
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
