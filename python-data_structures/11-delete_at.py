#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific index in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return list unchanged if idx is out of range

    del my_list[idx]  # Delete the element at the specified index
    return my_list  # Return the modified list
