#!/usr/bin/python3
"""
Validate utf-8
"""


def validUTF8(data):
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        num_bytes = 1
        leading_bits = data[i]

        for j in range(7, 1, -1):
            if leading_bits & (1 << j) == 0:
                break
            num_bytes += 1

        if num_bytes == 1:
            i += 1
            continue

        for j in range(1, num_bytes):
            if i + j >= len(data) or not is_continuation(data[i + j]):
                return False
        i += num_bytes

    return True
