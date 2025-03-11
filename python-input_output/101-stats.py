#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.

Expected input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Every 10 lines and after a keyboard interruption (CTRL + C), the script prints:
- Total file size: sum of all file sizes received
- Count of status codes received, sorted in ascending order

Only these status codes are tracked: 200, 301, 400, 401, 403, 404, 405, 500
"""

import sys

def print_stats(total_size, status_counts):
    """Prints the computed metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

total_size = 0
line_count = 0
status_counts = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) < 7:
            continue
        
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
