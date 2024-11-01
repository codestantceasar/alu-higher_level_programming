#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1  # Increment count if an integer is printed
        except (ValueError, TypeError):
            # Skip non-integer values silently
            continue
        except IndexError:
            # If x is larger than the list, raise the exception
            raise
    print("")  # Move to the next line after printing
    return count  # Return the number of integers printed
