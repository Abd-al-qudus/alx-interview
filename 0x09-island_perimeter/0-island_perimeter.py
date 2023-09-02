#!/usr/bin/python3
"""get the perimeter of the island of 0 and 1,
    the logic is to get the row length and column length.
    the perimeter is then defined by
    perimeter = 2 x (row-length + col-length)"""


def island_perimeter(grid):
    """return the perimeter of the island in the grid"""
    row, stat_row = 0, 0
    col, stat_col = 0, 0
    for object in grid:
        for symbol in object:
            if symbol == 1:
                row += 1
        if row > stat_row:
            stat_row = row
        row = 0

    i = 0
    while i < len(grid[0]):
        for j in range(len(grid)):
            if grid[j][i] == 1:
                col += 1
        if col > stat_col:
            stat_col = col
        col = 0
        i += 1

    return 2 * (stat_col + stat_row)
