def minPath(grid, k):
    n = len(grid)
    positions = {}

    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    neighbors = {}
    for i in range(n):
        for j in range(n):
            cells = []
            if i > 0:
                cells.append(grid[i - 1][j])
            if i < n - 1:
                cells.append(grid[i + 1][j])
            if j > 0:
                cells.append(grid[i][j - 1])
            if j < n - 1:
                cells.append(grid[i][j + 1])
            neighbors[grid[i][j]] = cells

    current = [min(positions)]
    path = [current[0]]

    for _ in range(k - 1):
        next_value = min(
            neighbor
            for value in current
            for neighbor in neighbors[value]
        )
        current = [
            value
            for value in set(
                neighbor
                for v in current
                for neighbor in neighbors[v]
            )
            if value == next_value
        ]
        path.append(next_value)

    return path