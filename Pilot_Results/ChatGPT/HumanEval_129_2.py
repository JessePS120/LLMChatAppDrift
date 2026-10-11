def minPath(grid, k):
    n = len(grid)
    positions = {}

    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    start = min(positions)
    r, c = positions[start]
    path = [start]

    if k == 1:
        return path

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(k - 1):
        candidates = []

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                candidates.append((grid[nr][nc], nr, nc))

        value, r, c = min(candidates)
        path.append(value)

    return path