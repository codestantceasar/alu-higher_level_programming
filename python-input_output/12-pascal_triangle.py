#!/usr/bin/python3
"""
pascal_triangle - Generates Pascal's Triangle up to a specified number of rows.

This module contains a function `pascal_triangle(n)` which generates Pascal's
Triangle. The first and last numbers of each row are 1, and each inner number
is the sum of the two numbers directly above it in the previous row.

Function:
    - pascal_triangle(n): Returns a list of lists representing Pascal's
      Triangle up to the `n`-th row.

Example:
    pascal_triangle(5) returns:
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the `n`-th row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle. If `n <= 0`,
              an empty list is returned.

    Example:
        pascal_triangle(3) returns:
            [
                [1],
                [1, 1],
                [1, 2, 1]
            ]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # Start with 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End with 1
        triangle.append(row)

    return triangle
