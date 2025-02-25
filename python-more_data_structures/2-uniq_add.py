#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list, counting each integer only once.

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The sum of all unique integers in the list.
    """
    unique_numbers = []
    total_sum = 0
    
    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
            total_sum += num
    
    return total_sum
