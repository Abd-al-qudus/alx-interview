## UTF-8 Validation algorithm
To determine if a given data set represents a valid UTF-8 encoding, we need to check the following rules for each byte in the data set:

    If the byte starts with '0', it represents a 1-byte character.
    If the byte starts with '110', it represents a 2-byte character.
    If the byte starts with '1110', it represents a 3-byte character.
    If the byte starts with '11110', it represents a 4-byte character.
    If the byte starts with '10', it is part of a multi-byte character and should not appear at the beginning.

If the above conditions are satisfied for each byte in the data set, then the data set represents a valid UTF-8 encoding.
