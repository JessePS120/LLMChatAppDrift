def minPath(grid, k):
    n = len(grid)
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                start_r, start_c = r, c
                break
    
    queue = [([1], start_r, start_c)]
    
    for _ in range(k - 1):
        next_dict = {}
        for path, r, c in queue:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_path = path + [grid[nr][nc]]
                    state = (nr, nc)
                    if state not in next_dict or new_path < next_dict[state]:
                        next_dict[state] = new_path
        queue = [(p, r, c) for (r, c), p in next_dict.items()]
    
    min_p = queue[0][0]
    for p, _, _ in queue:
        if p < min_p:
            min_p = p
    return min_p