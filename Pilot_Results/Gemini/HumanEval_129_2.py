def minPath(grid, k):
    n = len(grid)
    r, c = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                r, c = i, j
                break
        else:
            continue
        break
    
    path = [1]
    for _ in range(k - 1):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append((grid[nr][nc], nr, nc))
        val, r, c = min(neighbors)
        path.append(val)
    return path