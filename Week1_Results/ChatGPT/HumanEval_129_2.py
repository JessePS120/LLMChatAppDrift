def minPath(grid, k):
    n = len(grid)
    positions = [None] * (n * n + 1)

    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    start = min(
        range(1, n * n + 1),
        key=lambda v: v
    )
    r, c = positions[start]
    path = [start]

    if k == 1:
        return path

    neighbors = {}
    for i in range(n):
        for j in range(n):
            neighbors[(i, j)] = [
                (x, y)
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                if 0 <= x < n and 0 <= y < n
            ]

    current = (r, c)
    for _ in range(k - 1):
        current = min(
            neighbors[current],
            key=lambda pos: grid[pos[0]][pos[1]]
        )
        path.append(grid[current[0]][current[1]])

    return path