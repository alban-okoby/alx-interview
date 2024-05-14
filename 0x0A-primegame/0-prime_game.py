#!/usr/bin/python3

""" Prime Game """


def isWinner(x, nums):
    def sieve_of_eratosthenes(max_num):
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if (is_prime[p] == True):
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        return is_prime

    def simulate_game(n):
        is_prime = sieve_of_eratosthenes(n)
        p_nbs = [i for i in range(2, n + 1) if is_prime[i]]

        player_turn = 0
        while p_nbs:
            selected_prime = p_nbs[0]
            p_nbs = [num for num in p_nbs if num % selected_prime != 0]
            player_turn = 1 - player_turn

        return player_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
