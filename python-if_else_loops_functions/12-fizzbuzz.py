#!/usr/bin/python3
def fizzbuzz():
    """Print numbers from 1 to 100 with FizzBuzz rules."""
    for n in range(1, 101):
        if n % 15 == 0:
            print("FizzBuzz", end=' ')
        elif n % 3 == 0:
            print("Fizz", end=' ')
        elif n % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{}".format(n), end=' ')
