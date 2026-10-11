def minPath(grid, k):
    n = len(grid)
    current_paths = []
    for r in range(n):
        for c in range(n):
            current_paths.append(([grid[r][c]], r, c))
    
    for _ in range(k - 1):
        next_paths = []
        for path, r, c in current_paths:
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < n and 0 <= nc < n:
                    next_paths.append((path + [grid[nr][nc]], nr, nc))
        
        if not next_paths:
            break
        
        # Find the minimum value at the next step across all paths
        min_next_val = min(p[0][-1] for p in next_paths)
        # Filter paths that have the minimum value at the current step
        current_paths = [p for p in next_paths if p[0][-1] == min_next_val]
        
    # Sort paths lexicographically and return the first one's value list
    current_paths.sort(key=lambda x: x[0])
    return current_paths[0][0]