#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set of elements that are common to both sets.
    """
    return set_1 & set_2
