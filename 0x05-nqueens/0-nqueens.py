#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed on the specific position"""
    # Check row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < len(board):
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(n):
    """Solve the N Queens problem"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []

    def solve(col):
        """Recursive function to solve N Queens"""
        if col == n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
