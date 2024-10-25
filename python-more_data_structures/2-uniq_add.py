#!/usr/bin/python3


def uniq_add(my_list=[]):
    # Convert the list to a set to get unique values, then sum them
    unique_values = set(my_list)
    total_sum = sum(unique_values)
    return total_sum
