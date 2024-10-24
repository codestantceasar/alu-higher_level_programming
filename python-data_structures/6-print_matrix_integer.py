#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists of int): The matrix to print.
    """
    for row in matrix:
        if row:
            formatted_row = ' '.join("{:d}".format(num) for num in row)
            print(formatted_row)
