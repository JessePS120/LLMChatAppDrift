def minPath(grid, k):
    n = len(grid)
    positions = {}

    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    start = min(positions)
    path = [start]

    if k == 1:
        return path

    r, c = positions[start]
    neighbors = []

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            neighbors.append(grid[nr][nc])

    current = min(neighbors)
    path.append(current)

    for _ in range(k - 2):
        r, c = positions[current]
        neighbors = []

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append(grid[nr][nc])

        current = min(neighbors)
        path.append(current)

    return path