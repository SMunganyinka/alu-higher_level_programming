#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element with another in a new list.

    Args:
        my_list (list): The initial list.
        search (any): The element to replace.
        replace (any): The new element to replace with.

    Returns:
        list: A new list with replaced values.
    """
    return [replace if item == search else item for item in my_list]
