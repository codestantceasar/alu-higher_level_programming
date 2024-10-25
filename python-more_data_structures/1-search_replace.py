#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list where each occurrence of 'search' is replaced by 'replace'
    return [replace if x == search else x for x in my_list]
