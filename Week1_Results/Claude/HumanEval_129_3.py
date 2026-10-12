def minPath(grid, k):
    n = len(grid)
    
    start = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start = (i, j)
                break
        if start:
            break
    
    result = None
    
    def dfs(row, col, path):
        nonlocal result
        
        if len(path) == k:
            if result is None or path < result:
                result = path[:]
            return
        
        if result is not None and path >= result[:len(path)]:
            return
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n:
                path.append(grid[nr][nc])
                dfs(nr, nc, path)
                path.pop()
    
    dfs(start[0], start[1], [grid[start[0]][start[1]]])
    return result