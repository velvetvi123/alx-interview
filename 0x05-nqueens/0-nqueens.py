#!/usr/bin/python3
"""N queens solution finder module."""

import sys

def get_input():
    """Retrieves and validates the program's argument.
    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(pos1, pos2):
    """Checks if two queens are in an attacking position.
    Args:
        pos1 (list): [row, col] position of the first queen.
        pos2 (list): [row, col] position of the second queen.
    Returns:
        bool: True if queens are in an attacking position; False otherwise.
    """
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])

def solve_nqueens(n):
    """Uses backtracking to find all solutions for N queens problem.
    Args:
        n (int): Size of the chessboard.
    Returns:
        list: All valid solutions where no two queens attack each other.
    """
    solutions = []
    
    def backtrack(row, queens):
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            pos = [row, col]
            if all(not is_attacking(pos, q) for q in queens):
                queens.append(pos)
                backtrack(row + 1, queens)
                queens.pop()

    backtrack(0, [])
    return solutions

# Main Execution
n = get_input()
solutions = solve_nqueens(n)
for solution in solutions:
    print(solution)

