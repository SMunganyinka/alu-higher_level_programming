#!/usr/bin/python3
"""
Module: pascal_triangle

This module defines a function to generate Pascal's Triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    
    Example:
        pascal_triangle(5) -> [
                                [1],
                                [1, 1],
                                [1, 2, 1],
                                [1, 3, 3, 1],
                                [1, 4, 6, 4, 1]
                            ]
    """
    
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for row_num in range(1, n):
        row = [1]
        
        for j in range(1, row_num):
            row.append(triangle[row_num - 1][j - 1] + triangle[row_num - 1][j])
        
        row.append(1)
        triangle.append(row)
    
    return triangle
