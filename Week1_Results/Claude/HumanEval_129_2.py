def minPath(grid, k):
    n = len(grid)
    
    pos = {}
    for i in range(n):
        for j in range(n):
            pos[grid[i][j]] = (i, j)
    
    start_i, start_j = pos[1]
    
    min_path = None
    
    def dfs(i, j, path):
        nonlocal min_path
        
        if len(path) == k:
            if min_path is None or path < min_path:
                min_path = path[:]
            return
        
        if min_path is not None and path > min_path[:len(path)]:
            return
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                path.append(grid[ni][nj])
                dfs(ni, nj, path)
                path.pop()
    
    dfs(start_i, start_j, [grid[start_i][start_j]])
    return min_path