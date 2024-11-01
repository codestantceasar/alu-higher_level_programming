#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # Initialize the list to store division results
    for i in range(list_length):
        try:
            # Attempt to access elements at index i
            a = my_list_1[i]
            b = my_list_2[i]
            # Attempt to perform division
            result = a / b
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            # Append the result to new_list regardless of exceptions
            new_list.append(result)
    return new_list
