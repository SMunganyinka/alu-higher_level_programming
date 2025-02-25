#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral as a string.

    Returns:
        int: The integer representation, or 0 if input is invalid.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(roman_string):  # Iterate from right to left
        value = roman_values.get(char, 0)  # Get the value or default to 0
        if value < prev_value:
            total -= value  # Subtract if a smaller numeral is before a larger one
        else:
            total += value  # Otherwise, add it
        prev_value = value  # Update previous value

    return total
