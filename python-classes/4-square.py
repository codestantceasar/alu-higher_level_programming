#!/usr/bin/python3
"""Defines a class Square with size property."""


class Square:
    """Represents a square with size property."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size of the new square. Defaults to 0.
        """
        self.size = size  # Use the setter to validate size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The new size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
