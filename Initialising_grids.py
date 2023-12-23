"""
This tutorial shows you how to initialise a grid using list comprehension
The second example shows how you can use graphics to improve the user experience
"""

# Example 1 - Initialising a grid:
def initialise_grid(rows, cols):
    return [[" " for _ in range(cols)] for _ in range(rows)]

new_grid = initialise_grid(5,5)
for row in new_grid:
    print(row)

# The number of rows and columns are hard-coded when the function was called.
# However, you can get user input for these values instead as seen in Example 2.


# Example 2 - Creating a grid with while considering the user experience:
def display_board(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))

rows = int(input("How many rows? "))
cols = int(input("How many columns? "))

display_board(initialise_grid(rows, cols))