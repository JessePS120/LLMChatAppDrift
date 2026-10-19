def minPath(grid, k):
    n = len(grid)
    memo = {}
    
    def dfs(r, c, remaining):
        if remaining == 1:
            return [grid[r][c]]
        
        if (r, c, remaining) in memo:
            return memo[(r, c, remaining)]
        
        candidates = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                sub_path = dfs(nr, nc, remaining - 1)
                candidates.append(sub_path)
        
        best_sub_path = min(candidates)
        result = [grid[r][c]] + best_sub_path
        
        memo[(r, c, remaining)] = result
        return result
    
    all_paths = []
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, k)
            all_paths.append(path)
    
    return min(all_paths)