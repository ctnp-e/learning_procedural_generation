from PIL import Image
import random


WIDTH = 600
HEIGHT = 400
SCALE = 6
SMOOTHING_PASSES = 4

WATER_COLOR = (50, 100, 200)
LAND_COLOR = (60, 170, 80)
FOREST_COLOR = (30, 120, 50)

# (threshold, value)
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
            r = random.random()

            for threshold, value in TERRAIN_LEVELS:
                if r >= threshold:
                    row.append(value)
                    break

        grid.append(row)

    return grid


def smooth_grid(grid: list[list[int]]) -> list[list[int]]:
    rows = len(grid)
    cols = len(grid[0])
    # create a new grid to store the smoothed values
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)] 

    for y in range(rows):
        for x in range(cols):
            total = 0
            count = 0

            # neighborhood scan
            # this includes the cell itself and all 8 surrounding cells
            # delta y (row offset) -> vertical scan
            for dy in (-1, 0, 1):
                # delta x (column offset) -> horizontal scan
                for dx in (-1, 0, 1):
                    # combine offsets to get neighbor coordinates
                    nx = x + dx
                    ny = y + dy

                    '''
                    (x-1, y-1)  (x, y-1)  (x+1, y-1)
                    (x-1, y)    (x, y)    (x+1, y)
                    (x-1, y+1)  (x, y+1)  (x+1, y+1)
                    '''

                    # bound check to avoid out of range errors
                    # Only valid neighbors are considered in avg
                    if 0 <= nx < cols and 0 <= ny < rows:
                        
                        
                        # This includes the center cell itself (dx = 0, dy = 0)
                        # if you want to exclude it, make sure to add 
                        '''
                        if dx == 0 and dy == 0:
                            continue
                        '''

                        total += grid[ny][nx]   # add neighbor value to total
                        count += 1              # its an avg, what do you think? lol

            
            # Each cell becomes influenced by its surrounding cells.
            avg = total / count


            # map back to discrete terrain
            if avg < 0.5:
                new_grid[y][x] = 0      # water
            elif avg < 1.3:
                new_grid[y][x] = 1      # land
            else:
                new_grid[y][x] = 2      # mountain

    return new_grid

# generally grid -> image
def grid_to_image(grid: list[list[int]], scale: int) -> Image.Image:
    rows = len(grid)
    cols = len(grid[0])
    width = cols * scale
    height = rows * scale

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    for y in range(rows):
        for x in range(cols):
            # basic switch statement to map terrain type to color
            switch = {
                0: WATER_COLOR,
                1: LAND_COLOR,
                2: FOREST_COLOR
            }

            color = switch.get(grid[y][x], (0, 0, 0))
            for py in range(y * scale, (y + 1) * scale):
                for px in range(x * scale, (x + 1) * scale):
                    pixels[px, py] = color

    return image

# basic, you don't really edit it 
def main() -> None:
    cols = WIDTH // SCALE
    rows = HEIGHT // SCALE

    grid = make_grid(cols, rows)

    for i in range(SMOOTHING_PASSES):
        grid = smooth_grid(grid)

    print (grid)
    img = grid_to_image(grid, SCALE)
    img.show()


if __name__ == "__main__":
    main()