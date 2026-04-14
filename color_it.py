from PIL import Image

# image colors stored here
# better to put them all in one place but we leave it as is for now

WATER_COLOR = (50, 100, 200)
LAND_COLOR = (60, 170, 80)
FOREST_COLOR = (30, 120, 50)

def grid_to_image(grid: list[list[int]], width: int, height: int, scale: int) -> Image.Image:
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
