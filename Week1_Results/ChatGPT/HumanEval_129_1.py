def minPath(grid, k):
    n = len(grid)
    positions = {grid[i][j]: (i, j) for i in range(n) for j in range(n)}
    start = min(positions)
    path = [start]
    i, j = positions[start]

    while len(path) < k:
        neighbors = []
        if i > 0:
            neighbors.append((grid[i - 1][j], i - 1, j))
        if i + 1 < n:
            neighbors.append((grid[i + 1][j], i + 1, j))
        if j > 0:
            neighbors.append((grid[i][j - 1], i, j - 1))
        if j + 1 < n:
            neighbors.append((grid[i][j + 1], i, j + 1))

        value, i, j = min(neighbors)
        path.append(value)

    return path