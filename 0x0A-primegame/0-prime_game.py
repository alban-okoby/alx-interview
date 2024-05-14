#!/usr/bin/python3

""" Prime Game """


def prime_numbers_up_to(n):
    """ List of prime numbers up to 'n' using the Sieve of Eratosthenes """
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """ Winner of the Prime Game for given rounds and upper limits """
    if x is None or nums is None or x == 0 or not nums:
        return None
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = prime_numbers_up_to(n)
        remaining_numbers = set(range(1, n + 1))
        current_player = 'Maria'
        while remaining_numbers:
            playable_primes = [p for p in primes if p in remaining_numbers]
            if not playable_primes:
                break
            # Who is the winner of this turn ?
            if current_player == 'Maria':
                current_player = 'Ben'
            else:
                current_player = 'Maria'
            # smallest playable prime and remove its multiples
            chosen_prime = min(playable_primes)
            for multiple in range(chosen_prime, n + 1, chosen_prime):
                if multiple in remaining_numbers:
                    remaining_numbers.remove(multiple)
        if current_player == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
