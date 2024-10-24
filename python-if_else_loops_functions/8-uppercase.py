#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    result = ''
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper_c = chr(ord(c) - 32)
        else:
            upper_c = c
        result += upper_c
    print("{}".format(result))
