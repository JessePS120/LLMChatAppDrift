def minPath(grid, k):
    n = len(grid)
    best = {}
    for r in range(n):
        for c in range(n):
            best[(r, c)] = [grid[r][c]]
    for _ in range(2, k + 1):
        new_best = {}
        for r in range(n):
            for c in range(n):
                min_p = None
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        p = best[(nr, nc)] + [grid[r][c]]
                        if min_p is None or p < min_p:
                            min_p = p
                new_best[(r, c)] = min_p
        best = new_best
    ans = None
    for r in range(n):
        for c in range(n):
            if ans is None or best[(r, c)] < ans:
                ans = best[(r, c)]
    return ans