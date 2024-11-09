#!/usr/bin/python3
"""Defines a class BaseGeometry with a method that raises an Exception."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an Exception with a message indicating that the area."""
        raise Exception("area() is not implemented")
