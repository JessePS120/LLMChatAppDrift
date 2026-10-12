def minPath(grid, k):
    n = len(grid)
    r, c = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                r, c = i, j
                break
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            neighbors.append(grid[nr][nc])
    min_neighbor = min(neighbors) if neighbors else 1
    
    res = []
    for i in range(k):
        if i % 2 == 0:
            res.append(1)
        else:
            res.append(min_neighbor)
    return res