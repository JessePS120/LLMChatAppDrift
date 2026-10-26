def minPath(grid, k):
    n = len(grid)
    
    start_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_pos = (i, j)
                break
    
    min_path = None
    
    def dfs(row, col, path):
        nonlocal min_path
        
        if len(path) == k:
            if min_path is None or path < min_path:
                min_path = path[:]
            return
        
        if min_path is not None and path >= min_path[:len(path)]:
            return
        
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append((grid[nr][nc], nr, nc))
        
        neighbors.sort()
        
        for val, nr, nc in neighbors:
            path.append(val)
            dfs(nr, nc, path)
            path.pop()
    
    dfs(start_pos[0], start_pos[1], [1])
    return min_path