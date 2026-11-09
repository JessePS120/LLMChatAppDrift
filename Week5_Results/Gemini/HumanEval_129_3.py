def minPath(grid, k):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_r, start_c = i, j
                break
    
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = start_r + dr, start_c + dc
        if 0 <= nr < n and 0 <= nc < n:
            neighbors.append(grid[nr][nc])
            
    if k == 1:
        return [1]
        
    min_neighbor = min(neighbors)
    path = [1, min_neighbor]
    
    for step in range(2, k):
        if step % 2 == 0:
            path.append(1)
        else:
            path.append(min_neighbor)
            
    return path