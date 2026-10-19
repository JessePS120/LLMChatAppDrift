def minPath(grid, k):
    n = len(grid)
    
    start_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_pos = (i, j)
                break
    
    min_path = None
    
    def dfs(i, j, path):
        nonlocal min_path
        
        if len(path) == k:
            if min_path is None or path < min_path:
                min_path = path[:]
            return
        
        if min_path is not None and path >= min_path[:len(path)]:
            return
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                path.append(grid[ni][nj])
                dfs(ni, nj, path)
                path.pop()
    
    dfs(start_pos[0], start_pos[1], [1])
    
    return min_path