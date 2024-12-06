#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island
in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (List[List[int]]): A list of list of integers where:
                            0 represents water
                            1 represents land

    Returns:
    int: The perimeter of the island

    The function assumes:
    - The grid is rectangular, with width and height not exceeding 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing)
    - The island doesn't have "lakes"
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides for each land cell

                # Check and subtract for adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
