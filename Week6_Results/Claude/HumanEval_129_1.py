def minPath(grid, k):
    n = len(grid)
    pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                pos = (i, j)
    result = [1]
    i, j = pos
    for _ in range(k - 1):
        best = None
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if best is None or grid[ni][nj] < grid[best[0]][best[1]]:
                    best = (ni, nj)
        i, j = best
        result.append(grid[i][j])
    return result