#!/usr/bin/python3

""" Prime Game """


def isWinner(x, nums):
    def sieve_of_eratosthenes(max_num):
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if (is_prime[p]):
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, max_num + 1) if is_prime[p]]
        return prime_numbers

    max_n = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_n)

    def play_game(n, primes):
        remaining_numbers = set(range(1, n + 1))
        current_player = 0

        while True:
            can_move = False
            for prime in primes:
                if prime in remaining_numbers:
                    can_move = True
                    multiples = set(range(prime, n + 1, prime))
                    remaining_numbers -= multiples

                    if not remaining_numbers:
                        return current_player

                    break
            if not can_move:
                return 1 - current_player

            current_player = 1 - current_player

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        n = nums[i]
        primes_up_to_n = [p for p in prime_numbers if p <= n]
        winner = play_game(n, primes_up_to_n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
