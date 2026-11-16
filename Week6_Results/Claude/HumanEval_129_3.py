def minPath(grid, k):
    n = len(grid)
    best = None
    for i in range(n):
        for j in range(n):
            dp = {(i, j): [[grid[i][j]]]}
            for _ in range(k - 1):
                nxt = {}
                for (r, c), paths in dp.items():
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            for p in paths:
                                nxt.setdefault((nr, nc), []).append(p + [grid[nr][nc]])
                dp = {}
                for pos, paths in nxt.items():
                    dp[pos] = [min(paths)]
            for paths in dp.values():
                for p in paths:
                    if best is None or p < best:
                        best = p
            if k == 1:
                cand = [grid[i][j]]
                if best is None or cand < best:
                    best = cand
    return best