def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    min_path = None
    def dfs(r, c, path):
        nonlocal min_path
        if len(path) == k:
            if min_path is None or path < min_path:
                min_path = path
            return
        if min_path is not None and path >= min_path[:len(path)]:
            return
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                dfs(nr, nc, path + [grid[nr][nc]])
    for i in range(n):
        for j in range(n):
            dfs(i, j, [grid[i][j]])
    return min_path