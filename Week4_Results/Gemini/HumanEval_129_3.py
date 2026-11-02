def minPath(grid, k):
    n = len(grid)
    pos = {}
    for r in range(n):
        for c in range(n):
            pos[grid[r][c]] = (r, c)
    start_r, start_c = pos[1]
    paths = [[(start_r, start_c)]]
    for _ in range(k - 1):
        min_val = float('inf')
        next_states = []
        for path in paths:
            r, c = path[-1]
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    val = grid[nr][nc]
                    if val < min_val:
                        min_val = val
                        next_states = [(path + [(nr, nc)], (nr, nc))]
                    elif val == min_val:
                        next_states.append((path + [(nr, nc)], (nr, nc)))
        seen = set()
        paths = []
        for p, cell in next_states:
            if cell not in seen:
                seen.add(cell)
                paths.append(p)
    return [grid[r][c] for r, c in paths[0]]