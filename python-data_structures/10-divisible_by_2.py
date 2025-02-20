#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create a new list with True if the number is divisible by 2, False otherwise
    return [num % 2 == 0 for num in my_list]
