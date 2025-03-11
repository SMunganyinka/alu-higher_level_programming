#!/usr/bin/python3
"""This module is documented"""
import sys
from collections import defaultdict

# Dictionary to store counts for each status code
status_codes = defaultdict(int)
# Variable to accumulate the total file size
total_size = 0
# Counter for the number of lines processed
line_count = 0

def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    # Print the status codes in ascending order, if they exist
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")

# Read from stdin line by line
try:
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()
        
        # Extract the status code and file size
        if len(parts) >= 9:
            status_code = int(parts[8])
            file_size = int(parts[9])
            
            # Update metrics
            status_codes[status_code] += 1
            total_size += file_size
            line_count += 1
        
        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()
    sys.exit(0)
