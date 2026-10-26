def minPath(grid, k):
    n = len(grid)
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
            neighbors[grid[i][j]] = adj

    current = min(positions)
    path = [current]

    while len(path) < k:
        current = min(neighbors[current])
        path.append(current)

    return path