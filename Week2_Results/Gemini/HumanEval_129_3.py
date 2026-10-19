def minPath(grid, k):
    n = len(grid)
    r, c = -1, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                r, c = i, j
                break
        if r != -1:
            break
    
    path = [1]
    for _ in range(k - 1):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append((grid[nr][nc], nr, nc))
        min_val, nr, nc = min(neighbors)
        path.append(min_val)
        r, c = nr, nc
    return path