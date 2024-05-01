#!/usr/bin/python3

"""
Main program
"""

def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet the given total amount"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        while total >= coin:
            num_coins += 1
            total -= coin

    if total == 0:
        return num_coins
    else:
        return -1
