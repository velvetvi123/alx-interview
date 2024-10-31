#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (list): A list of integers representing bytes

    Returns:
        bool: True if valid UTF-8 encoding, False otherwise
    """
    # Track the number of continuation bytes expected
    continuation_bytes = 0

    for byte in data:
        # Only consider the 8 least significant bits
        byte = byte & 0b11111111

        # If we're expecting continuation bytes
        if continuation_bytes > 0:
            # Check if this is a valid continuation byte (starts with 10)
            if (byte >> 6) != 0b10:
                return False
            continuation_bytes -= 1

        # Check for 1-byte character (starts with 0)
        elif (byte >> 7) == 0:
            continuation_bytes = 0

        # Check for 2-byte character (starts with 110)
        elif (byte >> 5) == 0b110:
            continuation_bytes = 1

        # Check for 3-byte character (starts with 1110)
        elif (byte >> 4) == 0b1110:
            continuation_bytes = 2

        # Check for 4-byte character (starts with 11110)
        elif (byte >> 3) == 0b11110:
            continuation_bytes = 3

        # Invalid starting byte
        else:
            return False

    # Ensure all continuation bytes have been processed
    return continuation_bytes == 0
