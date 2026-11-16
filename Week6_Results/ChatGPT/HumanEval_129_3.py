def minPath(grid, k):
    n = len(grid)
    if k == 1:
        return [min(min(row) for row in grid)]

    min_val = min(min(row) for row in grid)
    r, c = next(
        (i, j)
        for i in range(n)
        for j in range(n)
        if grid[i][j] == min_val
    )

    path = [min_val]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(k - 1):
        candidates = [
            grid[nr][nc]
            for dr, dc in directions
            if 0 <= (nr := r + dr) < n
            and 0 <= (nc := c + dc) < n
        ]
        next_val = min(candidates)
        path.append(next_val)
        r, c = next(
            (r + dr, c + dc)
            for dr, dc in directions
            if 0 <= r + dr < n
            and 0 <= c + dc < n
            and grid[r + dr][c + dc] == next_val
        )

    return path