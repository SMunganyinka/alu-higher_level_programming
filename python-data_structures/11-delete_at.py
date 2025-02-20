#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list if index is out of range

    del my_list[idx]  # Use 'del' to remove the item at the index
    return my_list  # Return the modified list


# Test cases
my_list = [1, 2, 3, 4, 5]
print(delete_at(my_list[:], 3))  # Output: [1, 2, 3, 5]
print(delete_at(my_list[:], 0))  # Output: [2, 3, 4, 5]
print(delete_at(my_list[:], 4))  # Output: [1, 2, 3, 4]
print(delete_at(my_list[:], 5))  # Output: [1, 2, 3, 4, 5] (unchanged)
print(delete_at(my_list[:], -1))  # Output: [1, 2, 3, 4, 5] (unchanged)
print(delete_at([], 0))  # Output: [] (unchanged)
