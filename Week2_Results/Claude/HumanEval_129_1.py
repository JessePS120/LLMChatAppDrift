def minPath(grid, k):
    n = len(grid)
    
    start_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_pos = (i, j)
                break
    
    memo = {}
    
    def dfs(r, c, remaining):
        if remaining == 0:
            return []
        
        if remaining == 1:
            return [grid[r][c]]
        
        if (r, c, remaining) in memo:
            return memo[(r, c, remaining)]
        
        best_path = None
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                path = [grid[r][c]] + dfs(nr, nc, remaining - 1)
                if best_path is None or path < best_path:
                    best_path = path
        
        memo[(r, c, remaining)] = best_path
        return best_path
    
    return dfs(start_pos[0], start_pos[1], k)