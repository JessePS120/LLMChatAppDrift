def minPath(grid, k):
    n = len(grid)
    if k <= 0:
        return []

    positions = {}
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    min_value = min(positions)
    r, c = positions[min_value]
    path = [min_value]

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