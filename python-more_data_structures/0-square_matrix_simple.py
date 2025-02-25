#!/usr/bin/env python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a 2D matrix.
    
    Args:
        matrix (list of lists): A 2D list containing integers.

    Returns:
        list of lists: A new matrix with each value squared.
    """
    return [[num ** 2 for num in row] for row in matrix]

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)  # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
