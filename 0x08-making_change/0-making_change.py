#!/usr/bin/python3
"""Module to solve the Making Change Problem."""


def make_change(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations.
        total (int): The target amount to achieve using the coins.

    Returns:
        int: The fewest number of coins required, or -1 if it cannot be done.
    """
    if total <= 0:
        return 0

    accumulated_total = 0
    coins_used = 0
    coins = sorted(coins, reverse=True)

    for coin in coins:
        num_coins = (total - accumulated_total) // coin
        accumulated_total += num_coins * coin
        coins_used += num_coins
        if accumulated_total == total:
            return coins_used

    return -1

