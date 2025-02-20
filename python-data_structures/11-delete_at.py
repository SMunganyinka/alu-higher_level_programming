def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list if index is out of range

    del my_list[idx]  # Use 'del' to remove the item at the index
    return my_list  # Return the modified list

# Example usage
my_list = [1, 2, 3, 4, 5]
print(delete_at(my_list, 2))  # Output: [1, 2, 4, 5]
print(delete_at(my_list, -1))  # Output: [1, 2, 4, 5] (unchanged)
print(delete_at(my_list, 10))  # Output: [1, 2, 4, 5] (unchanged)
