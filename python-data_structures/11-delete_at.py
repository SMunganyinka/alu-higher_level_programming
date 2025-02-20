#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list  # If index is out of range, return the original list unchanged

    del my_list[idx]  # Delete the element at the specified index
    return my_list  # Return the modified list
