#!/usr/bin/python3
class MyList(list):
    """Class that inherits from list and prints the list sorted."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
