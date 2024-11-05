#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

# Attempt to create a square instance
print("Attempting to create a square...")
my_square = Rectangle.square(5)

# Check if the instance is None
if my_square is not None:
    print("Successfully created a square instance.")
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)
else:
    print("Failed to create a square instance.")
