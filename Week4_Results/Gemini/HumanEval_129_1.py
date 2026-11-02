def minPath(grid, k):
    n = len(grid)
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                sr, sc = r, c
                break
    ans = [n * n + 2] * k
    def dfs(r, c, path):
        nonlocal ans
        if len(path) == k:
            if path < ans:
                ans = path
            return
        if path >= ans[:len(path)]:
            return
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                dfs(nr, nc, path + [grid[nr][nc]])
    dfs(sr, sc, [1])
    return ans