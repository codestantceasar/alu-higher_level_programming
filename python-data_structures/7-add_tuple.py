#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements by padding with 0 if needed
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    
    # Get the first two elements from each tuple
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]
    
    # Return the result as a new tuple
    return (a1 + b1, a2 + b2)

# Test cases from the provided main.py file
if __name__ == "__main__":
    add_tuple = __import__('7-add_tuple').add_tuple

    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
