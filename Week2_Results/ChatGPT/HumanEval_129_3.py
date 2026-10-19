def minPath(grid, k):
    n = len(grid)
    positions = {}
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    start = min(range(1, n * n + 1))
    path = [start]
    r, c = positions[start]

    for _ in range(k - 1):
        neighbors = []
        if r > 0:
            neighbors.append((grid[r - 1][c], r - 1, c))
        if r < n - 1:
            neighbors.append((grid[r + 1][c], r + 1, c))
        if c > 0:
            neighbors.append((grid[r][c - 1], r, c - 1))
        if c < n - 1:
            neighbors.append((grid[r][c + 1], r, c + 1))

        value, r, c = min(neighbors)
        path.append(value)

    return path