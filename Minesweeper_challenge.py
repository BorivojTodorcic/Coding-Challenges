"""
MineSweeper Code Along Challenge

Given a Minesweeper-like grid represented by a list of lists.
The grid contains two types of cells: "-" for free spots and "#" for mines.
Your task is to create a program that takes this grid as input
and returns a copy of the grid where each "-" is replaced with a
number representing the count of mines in the surrounding cells
(including diagonals).


For the following input grid:
["-", "#", "-", "#", "#"],
["#", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "-", "-", "#"],
["#", "#", "-", "-", "-"]


The resulting output grid should be:
[2, "#", 3, "#", "#"],
["#", 3, 4, "#", "#"],
[2, "#", "2", 3, 3],
[2, 3, 2, 1, "#"],
["#", "#", 1, 1, 1]

"""


input_grid = [
    ["-", "#", "-", "#", "#"],
    ["#", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "-", "-", "#"],
    ["#", "#", "-", "-", "-"]
]

total_rows = len(input_grid)
total_cols = len(input_grid[0])


# Initialise a new grid:
output_grid = [[" " for _ in range(total_cols)] for _ in range(total_rows)]

# Loop through the input_grid:
for row in range(total_rows):
    for element in range(total_cols):
        # Add mines to output_grid in the same locations as input_grid
        if input_grid[row][element] == "#":
            output_grid[row][element] = "#"
        else:
            mine_counter = 0
            # Count the surrounding mines and set limits to avoid IndexErrors:
            for i in range(max(0, row - 1), min(total_rows, row + 2)):
                for j in range(max(0, element - 1), min(total_cols, element + 2)):
                    if input_grid[i][j] == "#":
                        mine_counter += 1
            output_grid[row][element] = mine_counter

# Print output_grid in matrix format
for total_rows in output_grid:
    print(total_rows)
