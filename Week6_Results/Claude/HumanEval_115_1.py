import math

def max_fill(grid, capacity):
    total = 0
    for row in grid:
        water = sum(row)
        total += math.ceil(water / capacity)
    return total