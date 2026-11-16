def minPath(grid, k):
    n = len(grid)
    best = None
    for i in range(n):
        for j in range(n):
            stack = [(i, j, [grid[i][j]])]
            while stack:
                r, c, path = stack.pop()
                if len(path) == k:
                    if best is None or path < best:
                        best = path
                    continue
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        stack.append((nr, nc, path + [grid[nr][nc]]))
    return best