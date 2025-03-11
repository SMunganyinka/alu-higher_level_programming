#!/usr/bin/python3
"""
Module: pascal_triangle

This module defines a function `pascal_triangle` that generates Pascal's Triangle
up to the nth row. The triangle is returned as a list of lists, where each list
represents a row of Pascal's Triangle.

The function handles edge cases where n <= 0 by returning an empty list.

Function:
    pascal_triangle(n): Generates Pascal's Triangle for a given n.
    
Usage Example:
    pascal_triangle(5) -> [
                            [1],
                            [1, 1],
                            [1, 2, 1],
                            [1, 3, 3, 1],
                            [1, 4, 6, 4, 1]
                        ]
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in the Pascal's Triangle to generate.

    Returns:
        list: A list of lists, where each list represents a row in Pascal's Triangle.
              An empty list is returned if n <= 0.
    
    Example:
        pascal_triangle(5) -> [
                                [1],
                                [1, 1],
                                [1, 2, 1],
                                [1, 3, 3, 1],
                                [1, 4, 6, 4, 1]
                            ]
    """
    
    # Base case: if n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate rows from 2 to n
    for row_num in range(1, n):
        # Start a new row with 1
        row = [1]
        
        # Fill in the intermediate values of the row
        for j in range(1, row_num):
            # Each element is the sum of the two elements above it
            row.append(triangle[row_num - 1][j - 1] + triangle[row_num - 1][j])
        
        # End the row with 1
        row.append(1)
        
        # Append the row to the triangle
        triangle.append(row)
    
    return triangle
