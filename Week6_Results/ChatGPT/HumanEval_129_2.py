def minPath(grid, k):
    n = len(grid)
    if k <= 0:
        return []

    positions = {}
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    neighbors = {}
    for i in range(n):
        for j in range(n):
            adj = []
            if i > 0:
                adj.append(grid[i - 1][j])
            if i < n - 1:
                adj.append(grid[i + 1][j])
            if j > 0:
                adj.append(grid[i][j - 1])
            if j < n - 1:
                adj.append(grid[i][j + 1])
            neighbors[grid[i][j]] = sorted(adj)

    current = min(positions)
    path = [current]

    for _ in range(k - 1):
        current = neighbors[current][0]
        path.append(current)

    return path