def minPath(grid, k):
    n = len(grid)
    positions = {}
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    start = min(
        range(1, n * n + 1),
        key=lambda v: v
    )
    r, c = positions[start]
    path = [start]

    for _ in range(k - 1):
        neighbors = []
        for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append((grid[nr][nc], nr, nc))

        value, r, c = min(neighbors)
        path.append(value)

    return path