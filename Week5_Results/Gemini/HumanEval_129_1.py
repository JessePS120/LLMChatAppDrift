def minPath(grid, k):
    n = len(grid)
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                sr, sc = r, c
                break
    nbrs = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = sr + dr, sc + dc
        if 0 <= nr < n and 0 <= nc < n:
            nbrs.append(grid[nr][nc])
    m = min(nbrs)
    return [1 if i % 2 == 0 else m for i in range(k)]