
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
