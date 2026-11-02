import math

def max_fill(grid, capacity):
    total = 0
    for row in grid:
        total += math.ceil(sum(row) / capacity)
    return total