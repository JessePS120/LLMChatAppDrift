def minPath(grid, k):
    n = len(grid)
    start_r, start_c = 0, 0
    found = False
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                start_r, start_c = r, c
                found = True
                break
        if found:
            break
            
    from collections import deque
    queue = deque([([1], start_r, start_c)])
    
    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append((nr, nc))
        return neighbors

    for _ in range(k - 1):
        cell_paths = {}
        while queue:
            path, r, c = queue.popleft()
            for nr, nc in get_neighbors(r, c):
                val = grid[nr][nc]
                new_path = path + [val]
                if (nr, nc) not in cell_paths or new_path < cell_paths[(nr, nc)]:
                    cell_paths[(nr, nc)] = new_path
        queue = deque([(p, r, c) for (r, c), p in cell_paths.items()])
        
    if k == 1:
        return [1]
        
    min_path = None
    while queue:
        path, r, c = queue.popleft()
        if min_path is None or path < min_path:
            min_path = path
            
    return min_path