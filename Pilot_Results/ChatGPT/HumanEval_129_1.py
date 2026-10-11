def minPath(grid, k):
    """
    Return the lexicographically smallest path of exactly k cells in the grid.
    """
    if k <= 0:
        return []

    n = len(grid)
    positions = {}
    for r in range(n):
        for c in range(n):
            positions[grid[r][c]] = (r, c)

    def neighbors(r, c):
        result = []
        if r > 0:
            result.append((r - 1, c))
        if r + 1 < n:
            result.append((r + 1, c))
        if c > 0:
            result.append((r, c - 1))
        if c + 1 < n:
            result.append((r, c + 1))
        return result

    start_value = min(positions)
    r, c = positions[start_value]
    path = [start_value]

    for _ in range(k - 1):
        next_cells = neighbors(r, c)
        r, c = min(next_cells, key=lambda pos: grid[pos[0]][pos[1]])
        path.append(grid[r][c])

    return path