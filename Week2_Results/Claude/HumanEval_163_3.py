def generate_integers(a, b):
    min_val = min(a, b)
    max_val = max(a, b)
    return [d for d in [2, 4, 6, 8] if min_val <= d <= max_val]