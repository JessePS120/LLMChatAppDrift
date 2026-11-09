def minPath(grid, k):
    n = len(grid)
    if k <= 0:
        return []

    positions = {}
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    def neighbors(value):
        i, j = positions[value]
        result = []
        if i > 0:
            result.append(grid[i - 1][j])
        if i < n - 1:
            result.append(grid[i + 1][j])
        if j > 0:
            result.append(grid[i][j - 1])
        if j < n - 1:
            result.append(grid[i][j + 1])
        return result

    current = [min(positions)]
    path = [current[0]]

    for _ in range(k - 1):
        candidates = []
        for value in current:
            candidates.extend(neighbors(value))

        smallest = min(candidates)
        current = [smallest]
        path.append(smallest)

    return path