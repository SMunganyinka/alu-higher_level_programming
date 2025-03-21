#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        pass  # Stop printing if index goes out of range
    print()  # Print a newline after the elements
    return count
