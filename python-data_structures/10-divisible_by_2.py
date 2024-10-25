#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    result_list = []
    for num in my_list:
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list


# Test cases from the provided main.py file
if __name__ == "__main__":
    divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        result_text = "is" if list_result[i] else "is not"
        print("{:d} {:s} divisible by 2".format(my_list[i], result_text))
        i += 1
