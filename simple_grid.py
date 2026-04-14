import random

TERRAIN_LEVELS = [
    (0.70, 2),
    (0.67, 1),
    (0.00, 0),
]

def make_grid(cols: int, rows: int) -> list[list[int]]:
    grid = []

    for _ in range(rows):
        row = []
        for _ in range(cols):

            # hold random value to touch it
            r = random.random()

            # iterate through terrain levels
            # find the first one that matches the random value
            for threshold, value in TERRAIN_LEVELS:

                # note this is going DOWN the list, 
                # so higher thresholds are checked first
                if r >= threshold:
                    row.append(value)
                    break # CUT IT SHORT
        grid.append(row)

    return grid

def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        print(' '.join(str(cell) for cell in row))
