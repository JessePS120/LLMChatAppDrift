def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    r, c = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] < val:
                val = grid[i][j]
                r, c = i, j
    
    neighbors = []
    if r > 0: neighbors.append(grid[r - 1][c])
    if r < n - 1: neighbors.append(grid[r + 1][c])
    if c > 0: neighbors.append(grid[r][c - 1])
    if c < n - 1: neighbors.append(grid[r][c + 1])
    
    mini = min(neighbors)
    
    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(val)
        else:
            ans.append(mini)
    return ans