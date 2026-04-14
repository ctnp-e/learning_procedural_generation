import color_it
import simple_grid
import smooth_brain

WIDTH = 600
HEIGHT = 400
SCALE = 6

ROWS = HEIGHT // SCALE
COLS = WIDTH // SCALE

grid = simple_grid.make_grid(COLS, ROWS)
grid = smooth_brain.smooth_grid(grid)
image = color_it.grid_to_image(grid, WIDTH, HEIGHT, SCALE)

image.show()


