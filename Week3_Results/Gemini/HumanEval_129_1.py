def minPath(grid, k):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                x, y = i, j
                break
    neighbors = []
    if x > 0:
        neighbors.append(grid[x - 1][y])
    if x < n - 1:
        neighbors.append(grid[x + 1][y])
    if y > 0:
        neighbors.append(grid[x][y - 1])
    if y < n - 1:
        neighbors.append(grid[x][y + 1])
    m = min(neighbors)
    return [1 if i % 2 == 0 else m for i in range(k)]