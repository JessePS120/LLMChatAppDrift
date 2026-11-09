def minPath(grid, k):
    n = len(grid)
    pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                pos = (i, j)
    i, j = pos
    result = [1]
    for _ in range(k - 1):
        best = None
        best_cell = None
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if best is None or grid[ni][nj] < best:
                    best = grid[ni][nj]
                    best_cell = (ni, nj)
        result.append(best)
        i, j = best_cell
    return result