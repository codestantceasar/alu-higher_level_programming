#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists of int): The matrix to print.
    """
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
