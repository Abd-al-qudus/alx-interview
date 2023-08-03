#!/usr/bin/env python3
"""this function validates a data whether it's
    correctly implemented utf-formatted or not,
    returns true and false otherwise"""

def validUTF8(data):
    """check data whether its a valid utf-8 string"""
    num_bytes_to_follow = 0

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if num_bytes_to_follow > 0:
            if byte >> 6 == 2:  # Check if the byte starts with '10'
                num_bytes_to_follow -= 1
            else:
                return False
        else:
            if byte >> 7 == 0:  # 1-byte character (starts with '0')
                num_bytes_to_follow = 0
            elif byte >> 5 == 6:  # 2-byte character (starts with '110')
                num_bytes_to_follow = 1
            elif byte >> 4 == 14:  # 3-byte character (starts with '1110')
                num_bytes_to_follow = 2
            elif byte >> 3 == 30:  # 4-byte character (starts with '11110')
                num_bytes_to_follow = 3
            else:
                return False
    # Check if all characters were properly closed
    return num_bytes_to_follow == 0
