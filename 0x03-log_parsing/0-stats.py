#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys


def print_stats(status_codes, total_size):
    """
    Print accumulated statistics
    Args:
        status_codes: dict of status codes and their count
        total_size: total file size
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()

        try:
            status_code = data[-2]
            file_size = int(data[-1])

            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size

        except (ValueError, IndexError):
            pass

        if line_count % 10 == 0:
            print_stats(status_codes, total_size)

except KeyboardInterrupt:
    print_stats(status_codes, total_size)
    raise

finally:
    print_stats(status_codes, total_size)
