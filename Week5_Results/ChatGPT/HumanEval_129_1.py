def minPath(grid, k):
    n = len(grid)
    positions = {}

    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    neighbors = {}
    for value, (i, j) in positions.items():
        neighbors[value] = []
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                neighbors[value].append(grid[ni][nj])

    start = min(positions)
    path = [start]

    for _ in range(k - 1):
        path.append(min(neighbors[path[-1]]))

    return path