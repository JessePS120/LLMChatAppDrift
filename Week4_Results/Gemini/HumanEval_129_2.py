def minPath(grid, k):
    n = len(grid)
    pos = {}
    for r in range(n):
        for c in range(n):
            pos[grid[r][c]] = (r, c)
    r, c = pos[1]
    path = [1]
    for _ in range(k - 1):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append(grid[nr][nc])
        min_val = min(neighbors)
        r, c = pos[min_val]
        path.append(min_val)
    return path