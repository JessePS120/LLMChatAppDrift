def minPath(grid, k):
    n = len(grid)
    
    start_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_pos = (i, j)
                break
        if start_pos:
            break
    
    min_path = None
    
    def dfs(i, j, path):
        nonlocal min_path
        
        if min_path and path > min_path:
            return
        
        if len(path) == k:
            if min_path is None or path < min_path:
                min_path = path[:]
            return
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                neighbors.append((grid[ni][nj], ni, nj))
        
        neighbors.sort()
        
        for val, ni, nj in neighbors:
            path.append(val)
            dfs(ni, nj, path)
            path.pop()
    
    dfs(start_pos[0], start_pos[1], [grid[start_pos[0]][start_pos[1]]])
    
    return min_path