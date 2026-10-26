def minPath(grid, k):
    n = len(grid)
    memo = {}
    
    def dfs(row, col, steps_left):
        if steps_left == 0:
            return []
        
        if (row, col, steps_left) in memo:
            return memo[(row, col, steps_left)]
        
        candidates = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n:
                sub_path = dfs(nr, nc, steps_left - 1)
                candidates.append([grid[nr][nc]] + sub_path)
        
        result = min(candidates) if candidates else []
        memo[(row, col, steps_left)] = result
        return result
    
    min_path = None
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]] + dfs(i, j, k - 1)
            if min_path is None or path < min_path:
                min_path = path
    
    return min_path