#!/usr/bin/python3

""" Prime Game """


def prime_numbers(n):
    """Return list of prime numbers between 1 and n inclusive
    Args:
        n (int): upper boundary of range. The lower boundary is always 1
    """
    prime_nos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if filtered[prime]:
            prime_nos.append(prime)
            for i in range(prime * prime, n + 1, prime):
                filtered[i] = False
    return prime_nos


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): number of rounds of the game
        nums (list): list of upper limits of range for each round
    Returns:
        Name of the winner (Maria or Ben) or None
    """
    if x is None or nums is None or x == 0 or not nums:
        return None

    maria = ben = 0
    for num in nums:
        prime_numbers_list = prime_numbers(num)
        if len(prime_numbers_list) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
