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
["#", 5, 5, "#", "#"],
[3, "#", "#", 5, 3],
[2, 3, 3, 4, "#"],
["#", "#", 3, 2, 2]

"""


input_grid = [
    ["-", "#", "-", "#", "#"],
    ["#", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "-", "-", "#"],
    ["#", "#", "-", "-", "-"]
]

rows = len(input_grid)
cols = len(input_grid[0])


# Initialise a new grid:
output_grid = [[" " for _ in range(cols)] for _ in range(rows)]

# Loop through the input_grid:
for row in range(rows):
    for element in range(cols):
        # Add mines to output_grid in the same locations as input_grid
        if input_grid[row][element] == "#":
            output_grid[row][element] = "#"
        else:
            # Count the surrounding mines
            mine_counter = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Set limits to avoid IndexErrors:
                    if (row + i < 0 or row + i >= rows) or (element + j < 0 or element + j >= cols):
                        pass
                    else:
                        if input_grid[row+i][element+j] == "#":
                            mine_counter += 1
                            output_grid[row][element] = mine_counter

# Print output_grid in matrix format
for rows in output_grid:
    print(rows)
