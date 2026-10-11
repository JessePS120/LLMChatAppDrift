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
            if i + 1 < n:
                adj.append(grid[i + 1][j])
            if j > 0:
                adj.append(grid[i][j - 1])
            if j + 1 < n:
                adj.append(grid[i][j + 1])
            neighbors[grid[i][j]] = sorted(adj)

    start = min(positions)
    path = [start]

    for _ in range(k - 1):
        path.append(neighbors[path[-1]][0])

    return path