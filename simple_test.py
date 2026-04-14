import color_it
import simple_grid

WIDTH = 600
HEIGHT = 400
SCALE = 6

ROWS = HEIGHT // SCALE
COLS = WIDTH // SCALE

grid = simple_grid.make_grid(COLS, ROWS)
image = color_it.grid_to_image(grid, WIDTH, HEIGHT, SCALE)

image.show()

