#!/usr/bin/python3
"""  Determines the number of minmum operations given n chars"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to give a result of exactly n H characters in a file
    Args:
        n: Number of characters to be displayed
    Returns:
        Number of minimum operations
    """

    current = 1
    start = 0
    counter = 0
    while current < n:
        remainder = n - current
        if remainder % current == 0:
            start = current
            current += start
            counter += 2
        else:
            current += start
            counter += 1
    return counter
