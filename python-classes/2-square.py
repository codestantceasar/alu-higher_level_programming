#!/usr/bin/python3
"""Defines a class Square with size validation."""


class Square:
    """Represents a square with size validation."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
