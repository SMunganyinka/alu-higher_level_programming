#!/usr/bin/python3


def max_integer(my_list=[]):
    # Return None if the list is empty
    if not my_list:
        return None
    
    # Initialize the first element of the list as the maximum
    max_num = my_list[0]
    
    # Iterate through the list and compare each number
    for num in my_list:
        if num > max_num:
            max_num = num
    
    return max_num
