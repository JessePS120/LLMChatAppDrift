def minPath(grid, k):
    n = len(grid)
    r, c = next((i, j) for i in range(n) for j in range(n) if grid[i][j] == 1)
    path = [1]
    for _ in range(k - 1):
        neighbors = [
            (r + dr, c + dc)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if 0 <= r + dr < n and 0 <= c + dc < n
        ]
        r, c = min(neighbors, key=lambda p: grid[p[0]][p[1]])
        path.append(grid[r][c])
    return path