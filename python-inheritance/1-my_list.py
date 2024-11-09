#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A subclass of list that can print its elements in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        sorted_list = sorted(self)
        print(sorted_list)
