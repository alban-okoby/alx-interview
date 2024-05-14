#!/usr/bin/python3

""" Prime Game """


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
    Args:
        n (int): upper boundary of range. 0r always 1
    """
    prime_numbers = []
    is_prime = [True] * (n + 1)
    for number in range(2, n + 1):
        if is_prime[number]:
            prime_numbers.append(number)
            for multiple in range(number, n + 1, number):
                is_prime[multiple] = False
    return prime_numbers


def isWinner(x, nums):
    """
    The winner of the Prime Game
    Args:
        x (int): number of rounds of the game
        nums (list): list of upper limits of range for each round
    Returns:
        Name of the winner or None
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        prime_numbers_list = primeNumbers(nums[i])
        if len(prime_numbers_list) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
