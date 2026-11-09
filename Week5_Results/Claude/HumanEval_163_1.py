def generate_integers(a, b):
    lo, hi = min(a, b), max(a, b)
    return [d for d in range(lo, hi + 1) if d < 10 and d % 2 == 0]