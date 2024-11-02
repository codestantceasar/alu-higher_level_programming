#!/usr/bin/python3
"""
Defines a Rectangle class with attributes and methods for calculating area,
perimeter, and representing the rectangle in string format.
"""

class Rectangle:
    """
    Represents a rectangle with width and height attributes.
    
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: Symbol used for string representation of the rectangle.
    """

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If either width or height is 0, perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns the string representation of the rectangle
        using the print_symbol attribute.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle instance
        that can be used to recreate the instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message and decrements the instance counter
        when the Rectangle instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles by area and returns the bigger one.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with equal width and height.

        Args:
            size (int): The size of the width and height of the square.

        Returns:
            Rectangle: A new Rectangle instance where width == height == size.
        """
        return cls(size, size)
