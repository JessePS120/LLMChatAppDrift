def minPath(grid, k):
    n = len(grid)
    positions = {}
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    start = min(grid[i][j] for i in range(n) for j in range(n))
    r, c = positions[start]
    path = [start]

    for _ in range(k - 1):
        neighbors = []
        if r > 0:
            neighbors.append((grid[r - 1][c], r - 1, c))
        if r + 1 < n:
            neighbors.append((grid[r + 1][c], r + 1, c))
        if c > 0:
            neighbors.append((grid[r][c - 1], r, c - 1))
        if c + 1 < n:
            neighbors.append((grid[r][c + 1], r, c + 1))

        value, r, c = min(neighbors)
        path.append(value)

    return path