#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary with integer values.

    Returns:
        dict: A new dictionary with values doubled.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
