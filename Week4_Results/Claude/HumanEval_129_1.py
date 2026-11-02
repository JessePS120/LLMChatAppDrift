def minPath(grid, k):
    n = len(grid)
    r, c = next((i, j) for i in range(n) for j in range(n) if grid[i][j] == 1)
    path = [1]
    for _ in range(k - 1):
        best = None
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if best is None or grid[nr][nc] < grid[best[0]][best[1]]:
                    best = (nr, nc)
        r, c = best
        path.append(grid[r][c])
    return path