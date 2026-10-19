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
        min_val = float('inf')
        next_r, next_c = -1, -1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] < min_val:
                    min_val = grid[nr][nc]
                    next_r, next_c = nr, nc
        r, c = next_r, next_c
        path.append(min_val)
    return path