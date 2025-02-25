#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a 2D matrix.
    
    Args:
        matrix (list of lists): A 2D list containing integers.

    Returns:
        list of lists: A new matrix with each value squared.
    """
    return [[num ** 2 for num in row] for row in matrix]  
