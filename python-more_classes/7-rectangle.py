#!/usr/bin/python3
"""Defines a Rectangle class with customizable print symbol."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: Symbol used for string representation.
    """

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"       # Public class attribute

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        type(self).number_of_instances += 1  # Increment instance count
        self.width = width    # Validated via the width setter
        self.height = height  # Validated via the height setter

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value  # Store the validated value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value  # Store the validated value

    def area(self):
        """Compute and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Compute and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle.

        The rectangle is represented using the symbol stored in print_symbol.

        Returns:
            str: The string representation of the rectangle, or an empty
            string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append(symbol * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string representation of the rectangle for reproduction.

        Returns:
            str: String to recreate an instance using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when an instance is deleted and decrement count."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1  # Decrement instance count
